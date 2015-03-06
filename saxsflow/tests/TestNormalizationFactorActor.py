'''
Created on 6 Mar 2015

@author: ademaria
'''
import unittest
import ConfigParser
from saxsflow.common.webservices import ispyb
from saxsflow.actors.normalisationactor import NormalisationActor


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

    def testRun(self):
        json = self.ispyb.getWorkflowByStatus("PENDING")
        actor = NormalisationActor(json)

        if len(actor.getDataset().getSubtractionFilePathList()) > 0:
            if len(actor.getDataset().getPDBfilePathList()) > 0:
                actor.run(actor.getDataset().getSubtractionFilePathList()[0], actor.getDataset().getPDBfilePathList()[0], actor.getDataset().getSubtractions(0)["exposureTemperature"])
        pass

if __name__ == "__main__":
    unittest.main()
