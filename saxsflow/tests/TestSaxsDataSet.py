'''
Created on 6 Mar 2015

@author: ademaria
'''
import unittest
from saxsflow.tests.SaxsFlowTestCase import SaxsFlowTestCase


class Test(SaxsFlowTestCase):

    def testSubtractionFilePathList(self):
        print(str(self.ds.getSubtractionFilePathList()))

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
