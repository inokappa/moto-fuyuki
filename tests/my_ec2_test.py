import sys
import os
import StringIO
import unittest
from moto import mock_ec2
from my_ec2 import get_client, list_ec2_instances, main

class Ec2TestCase(unittest.TestCase):

    def setUp(self):
        """
        setUp will run before execution of each test case
        """
        pass

    @mock_ec2
    def __moto_setup(self):
        """
        Run Instance
        """
        ec2 = get_client()
        reservation = ec2.run_instances(ImageId='ami-f00ba4', MinCount=1, MaxCount=1)
        self.instance_id = reservation['Instances'][0]['InstanceId']

    def tearDown(self):
        """
        tearDown will run after execution of each test case
        """
        pass

    @mock_ec2
    def test_get_client(self):
        """
        check that out get_client function has a valid endpoint
        """
        ec2 = get_client()
        self.assertEqual(ec2._endpoint.host, 'https://ec2.ap-northeast-1.amazonaws.com')

    @mock_ec2
    def test_list_ec2_instances(self):
        """
        check that our bucket shows as expected
        """
        instances = [e for e in list_ec2_instances()]
        self.assertEqual([], instances)

    @mock_ec2
    def test_main(self):
        """
        verifies the execution of the main function
        """
        # setup ec2 environment
        self.__moto_setup()

        # capture stdout for processing
        sys.stdout = mystdout = StringIO.StringIO()

        # run main function
        main()

        content = mystdout.getvalue()
        self.assertEqual(self.instance_id, content.strip())

# if __name__ == '__main__':
#     unittest.main()
