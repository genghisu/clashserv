from mock import Mock
from unittest2 import TestCase

from boto.ec2.connection import EC2Connection

from django_ec2.instance import InstanceManager

from django_ec2 import logger

class TestInstanceManager(TestCase):
    def setUp(self):
        """ set up the test case """
        if True:
            self.instanceManager = InstanceManager()
        else:
            self.conn = Mock(spec=['EC2Connection'])
            self.instanceManager = InstanceManager(connection=self.conn)

    def tearDown(self):
        """ tear down the test case """

    def testInstance(self):
        """ test getting a list of instances """
        instances = self.instanceManager.instances

        # instance list should be iterable
        self.assertTrue(instances.__iter__)
        for instance in instances:
            # instance should have an id, etc
            self.assertTrue(instance.id)
            # instance should have been added the formatInstance
            self.assertTrue(instance.formatted)
            logger.debug(instance.formatted)

