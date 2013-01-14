"""
Deployment toolbox for EC2
"""
from fabric.api import *

env.hosts = ['ubuntu@' + dns_name]
def deploy(self, dns_name):
    """deploy stuff"""
    logger.debug('env.hosts: ' + str(env.hosts))

    logger.info('Preparing to deploy to %s' %(dns_name,))
    #with settings(warn_only=True):
    #    local('bin/project', capture=False)
    run('ls')
