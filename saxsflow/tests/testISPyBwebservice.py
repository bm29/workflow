'''
Created on 6 Mar 2015

@author: ademaria
'''
import unittest
from saxsflow.common.webservices import ispyb
import ConfigParser


class Test(unittest.TestCase):
    ispyb = None

    def setUp(self):
        print("Setup client")
        # Reading configuration params
        config = ConfigParser.ConfigParser()
        config.read('../../conf/testing.conf')

        # Connection parameters
        url = config.get('Connection', 'url')
        username = config.get('Connection', 'user')
        password = config.get('Connection', 'password')

        self.ispyb = ispyb.ISPyB(url, username, password)
        pass

    def tearDown(self):
        print("Finished")
        pass

    def testGetWorkflowByStatus(self):
        print self.ispyb.getWorkflowByStatus("PENDING")
        pass

if __name__ == "__main__":
    unittest.main()
