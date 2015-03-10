'''
Created on 6 Mar 2015

@author: ademaria
'''
import unittest
from saxsflow.actors.crysol import Crysol
from saxsflow.tests.SaxsFlowTestCase import SaxsFlowTestCase


class TestCrysol(SaxsFlowTestCase):
    def testRun(self):
        actor = Crysol(self.json)
        actor.run(actor.getDataset().getSubtractionFilePathList()[0], actor.getDataset().getPDBfilePathList()[0])
        pass

if __name__ == "__main__":
    unittest.main()
