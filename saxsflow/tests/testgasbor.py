'''
Created on 6 Mar 2015

@author: ademaria
'''
import unittest
import ConfigParser
from saxsflow.common.webservices import ispyb
from saxsflow.actors.gasbor import Gasbor


class TestOligomer(unittest.TestCase):
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

    def testRun(self):
        json = self.ispyb.getWorkflowByStatus("PENDING")
        actor = Gasbor(json)
        actor.run()

if __name__ == "__main__":
    unittest.main()
