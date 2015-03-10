'''
Created on 6 Mar 2015

@author: ademaria
'''
import unittest
from saxsflow.actors.gnom import Gnom
from saxsflow.tests.SaxsFlowTestCase import SaxsFlowTestCase


class TestOligomer(SaxsFlowTestCase):
    def testRun(self):
        actor = Gnom(self.json)
        actor.run()

if __name__ == "__main__":
    unittest.main()
