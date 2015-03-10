'''
Created on 6 Mar 2015

@author: ademaria
'''
import unittest
from saxsflow.actors import pepsiSAXS
from saxsflow.tests.SaxsFlowTestCase import SaxsFlowTestCase


class TestPepsiSAXS(SaxsFlowTestCase):

    def testRun(self):
        actor = pepsiSAXS.PepsiSAXS(self.json)
        actor.run()

if __name__ == "__main__":
    unittest.main()
