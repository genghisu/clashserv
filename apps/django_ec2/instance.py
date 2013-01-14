"""
ec2.py provides the interfaces necessary to use amazon ec2 via Boto.

In order for boto to successfully connect to the correct AWS account, you will
need to set the appropriate environment variables containing the ACCESS_ID
and SECRET_KEY. These credentials can be obtained from the AWS security setup.

Perhaps add something like this to your $HOME/.profile:
export AWS_ACCESS_KEY_ID="AKIAIY..."
export AWS_SECRET_ACCESS_KEY="KSbns6..."

If you don't want your instances to go to the default ec2 region, you may
need to create a boto configuration file [1].

    [1] http://boto.cloudhackers.com/ec2_tut.html

"""

import time
import boto.ec2
from boto.ec2.connection import EC2Connection

from django_ec2 import logger

class InstanceManager(object):
    """
    A class to manage EC2 instances.
    """
    _defaultRegion = 'us-east-1'

    def __init__(self, connection=None):
        """
        Initialize the InstanceManager, allowing for dependency injection
        """
        if not connection:
            self.connection = EC2Connection()
        else:
            self.connection = connection

    def _getConnection(self, region=None):
        """
        get a connection to the default region endpoint
        """
        if not region:
            regionName = self._defaultRegion

        for region in boto.ec2.regions():
            if region.name == regionName:
                self.region = region
                logger.info('using region %s' %(str(region.name)))
                return self.region.connect()

    def _formatInstance(self, instance):
        """
        format an instance with relevant info
        """
        return "%(id)-10s %(instance_type)-10s %(image_id)-12s %(state)-8s %(dns_name)-20s" %(instance.__dict__)

    @property
    def instances(self):
        """
        list the instances available in the connection
        """
        reservations = self.connection.get_all_instances()
        instances = list()
        for r in reservations:
            for i in r.instances:
                i.formatted = self._formatInstance(i)
                instances.append(i)
        return instances
    
    #ami-2ec83147
    #ami-e4d42d8d
    #ami-ab36fbc2
    def launch(self, instance_type='t1.micro', 
               image_id='ami-ab36fbc2',
               key_name='picmobo',
               security_groups=('default', 'app_stack')):
        """
        launch an instance
        """
        image = self.connection.get_all_images(image_ids=(image_id,))[0]
        logger.debug('Got image %s' %(str(image)))
        security_groups = self.connection.get_all_security_groups(security_groups)
        logger.debug('Got security groups %s' %(str(security_groups)))
        kwargs = { 'instance_type':     instance_type, 
                   'key_name':          key_name,
                   'security_groups':   security_groups
                }
        logger.debug('Instantiating with kwargs = %s' %(str(kwargs)))
        reservation = image.run(**kwargs)
        instance = reservation.instances[0]
        while instance.state != 'running':
            logger.debug('State is %s, waiting...' %(instance.state,))
            time.sleep(10)
            instance.update()
        logger.info('Creating volumes')
        vol = self.connection.create_volume(10, instance.placement)
        vol.attach(instance.id, '/dev/sdf')
        vol = self.connection.create_volume(10, instance.placement)
        vol.attach(instance.id, '/dev/sdg')
        logger.info('EC2 launch of %s complete at %s' %(instance.id,
                                                        instance.dns_name))


    def terminate(self, instance_id):
        """
        terminate an instance
        """
        instance = self.get_instance(instance_id)
        if instance:
            logger.debug('Successfully connected to instance %s' %(instance_id),)
            instance.terminate()
            logger.info('Instance %s terminated' %(instance_id,))
        else:
            logger.warning('Instance %s not found' %(instance_id,))

    def get_instance(self, instance_id):
        """
        get a handle to an instance by id
        """
        return self.connection.get_all_instances((instance_id,))[0].instances[0]


    def get_external_dns_name(self, instance_id):
        """
        get the dns name for the specified instance
        """
        instance = self.get_instance(instance_id)
        return instance.dns_name

