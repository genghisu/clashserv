import sys

from django.core.management.base import BaseCommand, CommandError

from django_ec2.instance import InstanceManager
#from django_ec2.deploy import FabricDeployer

class Command(BaseCommand):
    args = '<command> <command args ...>'
    help = 'Run EC2 management commands'
    sub_commands = ('launch', 'list',)
    stdout = sys.stdout

    def handle(self, *args, **options):
        if len(args) < 1:
            raise CommandError('No command specified. Valid commands: %s'
                               %(str(self.sub_commands)))
        command = args[0]
        args = args[1:]
        self.stdout.write('Running %s with %s\n' %(command, str(args)))

        manager = InstanceManager()
        #deployer = FabricDeployer()
        if command == 'list':
            template = "%(id)-10s %(instance_type)-10s %(image_id)-12s %(dns_name)-20s\n" 
            self.stdout.write(template %({'id':                 'id', 
                                         'instance_type':      'type',
                                         'image_id':           'image_id',
                                         'dns_name':           'dns_name'
                                         }))
            for i in manager.instances:
                self.stdout.write(i.formatted + '\n')
        elif command == 'launch':
            manager.launch()
        elif command == 'terminate':
            (instance_id, ) = args
            manager.terminate(instance_id)
        elif command == 'deploy':
            (instance_id, ) = args
            external_ip = manager.get_external_dns_name(instance_id)
            #deployer.deploy(external_ip)



