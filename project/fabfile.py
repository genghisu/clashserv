"""
Deployment toolbox for EC2
"""
import os
import time

import logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger('fabfile')

from fabric.api import *
from fabric.contrib.files import *

svn_options='--non-interactive --trust-server-cert --username=build --password=thei1AeK  --no-auth-cache'
project_git_url = 'git@github.com:genghisu/lottserv.git'
project_dir = '/var/www/lottserv'

home_dir = None
remote_home_dir = '/home/ubuntu'

db_values = None

def development():
    global settings_file
    global db_values
    global home_dir
    global remote_dir
    
    env.user="ubuntu"
    env.key_filename=os.environ['HOME'] + "/.ssh/hanbox.pem"
    env.host_string = "50.17.254.117"
    settings_file = 'development_settings.py'
    remote_home_dir = '/home/ubuntu'
    home_dir = '/home/han'
    
    db_values = {
        'db_master_user':'genghisu',
        'db_master_password':'arcamdarien1234',
        'db_user': 'lottserv',
        'db_pass': 'lottserv',
        'db_name': 'lottserv',
        'db_host': 'localhost',
        'db_port': '5432',
        'project_dir': project_dir,
        'db_dump': '',
    }
    
def initialize():
    """
    initialize ebs volumes, etc. This is a destructive operation, use
    carefully
    """
    sudo('apt-get -y install lvm2')
    sudo('/sbin/modprobe dm_mod')
    append('/etc/modules', 'dm_mod', use_sudo=True)
    sudo('pvcreate /dev/sdf /dev/sdg')
    sudo('vgcreate vgMedia /dev/sdf')
    sudo('vgcreate vgPg /dev/sdg')
    sudo('lvcreate -n media -l 2559 vgMedia')
    sudo('lvcreate -n pgdata -l 2559 vgPg')
    sudo('echo "y\n" | mke2fs -j /dev/vgMedia/media')
    sudo('echo "y\n" | mke2fs -j /dev/vgPg/pgdata')
    sudo('mkdir -p /ebs/lottserv-media')
    append('/etc/fstab', '/dev/vgPg/pgdata /var/lib/postgres/8.4/main  auto    defaults    0 0',
           use_sudo=True)
    append('/etc/fstab', '/dev/vgMedia/media /ebs/lottserv-media    auto    defaults    0 0',
            use_sudo=True)
    sudo('mkdir -p /var/lib/postgres/8.4/main')
    sudo('mount /var/lib/postgres/8.4/main')
    sudo('mount /ebs/lottserv-media')

def prepare():
    """
    prepare env.hosts to serve django sites

    expects an ubuntu lucid platform. handles installing system-level
    dependencies and configuring them for autostart

    """
    sudo("""apt-get update""")
    sudo("""aptitude install -y --quiet=2 ntp \
         apache2 libapache2-mod-wsgi apache2-mpm-worker \
         postgresql-8.4 postgresql-8.4-postgis postgresql-client \
         python-psycopg2 libdbd-pg-perl \
         python-mysqldb \
         python-dev \
         sendmail \
         python-simplejson python-jinja2 python-crypto  python-setuptools \
         python-lxml \
         memcached python-memcache \
         git-core \
         lynx \
         """)
    sudo('a2enmod wsgi proxy_http status')
    append('ExtendedStatus On', '/etc/apache2/conf.d/extendedstatus.conf',
           use_sudo=True)
    sudo('update-rc.d apache2 enable')
    sudo('/etc/init.d/apache2 restart')

    sudo('update-rc.d postgresql-8.4 enable')
    sudo('/etc/init.d/postgresql-8.4 restart')

    sudo('update-rc.d memcached enable')
    sudo('/etc/init.d/memcached restart')

def reset_postgres():
    """
    reset the postgres database. use with caution.
    """
    db_values['tempdb'] = 'tempdb'
    db_values['tempfil'] = '/tmp/tempfil'
    append('$HOME/.pgpass', '*:*:%(db_name)-s:%(db_user)-s:%(db_pass)-s' %(db_values))
    run('chmod 0600 $HOME/.pgpass')
    with settings(warn_only=True):
        sudo('echo "drop database %(db_name)-s;" | psql' %(db_values), user='postgres')
        sudo('echo "drop user %(db_user)-s;" | psql' %(db_values), user='postgres')
    sudo('echo "create user %(db_user)-s with password \'%(db_pass)-s\';" | psql' %(
        db_values), user='postgres')
    sudo('echo "drop database tempdb" | psql', 
         user='postgres')
    sudo('echo "create database %(tempdb)-s" | psql' %(db_values), user='postgres')
    sudo('pg_dump -Fc --no-owner %(tempdb)-s --file %(tempfil)-s' %(db_values), 
         user='postgres')
    sudo('echo "drop database %(tempdb)-s" | psql' %(db_values), 
         user='postgres')
    sudo('echo "create database %(db_name)-s with owner %(db_user)-s" | psql' %(
        db_values), user='postgres')
    sudo('rm %(tempfil)-s' %(db_values))

def init_log():
    run('cd %s && touch test.log' %(project_dir))
    run('chmod 777 %s/test.log' %(project_dir))
    
def git_deploy():
    sudo('rm -rf %s' %(project_dir))
    sudo('mkdir %s' %(project_dir))
    sudo('chown %s %s' %(env.user, project_dir))
    run('git clone %s %s' % (project_git_url, project_dir))
    run('cd %s && python bootstrap.py' %(project_dir))
    init_log()
    reset_postgres()
    git_update()

def upload_ssh_keys():
    upload_template('%s/.ssh/id_rsa' % (home_dir),
                    '%s/.ssh/id_rsa' % (remote_home_dir))
    upload_template('%s/.ssh/id_rsa.pub' % (home_dir),
                    '%s/.ssh/id_rsa.pub' % (remote_home_dir))
    run('chmod 600 %s/.ssh/id_rsa' % (remote_home_dir))
    
def git_update():
    """
    update the site via git
    """
    run('cd %s && git pull origin master' %(project_dir))
    run('cd %s && bin/buildout' %(project_dir))
    upload_template(settings_file,
                    '%s/project/local_settings.py' %(project_dir), db_values)
    run('chmod 0644 %s/project/local_settings.py' %(project_dir))

    upload_template('apache2-default.conf',
                    '/etc/apache2/sites-available/default',
                    context = {'project_dir': project_dir, },
                    use_sudo=True
                   )
    sudo('/etc/init.d/apache2 stop')
    sudo("""
         touch /var/log/apache2/lottserv-wsgi.log
         chown www-data /var/log/apache2/lottserv-wsgi.log
         """
        )
    run('cd %s && bin/django syncdb' %(project_dir,))
    run('cd %s && bin/django migrate' %(project_dir,))
    sudo('/etc/init.d/apache2 start')

def full_deploy():
    """
    staged full deployment, from scratch.
    """
    initialize()
    prepare()
    git_deploy()
    