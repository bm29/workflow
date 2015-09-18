'''
Created on 6 Mar 2015

@author: ademaria
'''
import unittest
from saxsflow.common.webservices import ispyb
import ConfigParser
from saxsflow.tests.SaxsFlowTestCase import SaxsFlowTestCase


class Test(SaxsFlowTestCase):
    ispyb = None


    def tearDown(self):
        print("Finished")
        pass

    def testGetWorkflowByStatus(self):
        print self.ispyb.getWorkflowByStatus("PENDING")
        pass

if __name__ == "__main__":
    unittest.main()
