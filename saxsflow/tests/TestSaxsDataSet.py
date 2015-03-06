'''
Created on 6 Mar 2015

@author: ademaria
'''
import unittest
from saxsflow.common.webservices import ispyb
from saxsflow.data.saxsdataset import SaxsDataset
import ConfigParser


class Test(unittest.TestCase):
    ispyb = None

    def setUp(self):
        # Reading configuration params
        config = ConfigParser.ConfigParser()
        config.read('../../conf/testing.conf')

        # Connection parameters
        url = config.get('Connection', 'url')
        username = config.get('Connection', 'user')
        password = config.get('Connection', 'password')

        self.ispyb = ispyb.ISPyB(url, username, password)
        self.ds = SaxsDataset(self.ispyb.getWorkflowByStatus("PENDING"))
        pass

    def testSubtractionFilePathList(self):
        print(str(self.ds.getSubtractionFilePathList()))
        pass

    def testSubtractions(self):
        print(str(self.ds.getSubtractions()))
        pass

    def testMacromolecules(self):
        print(str(self.ds.getMacromolecules()))
        pass

    def testgetPDBfilePathList(self):
        print(str(self.ds.getPDBfilePathList()))
        pass

if __name__ == "__main__":
    unittest.main()
