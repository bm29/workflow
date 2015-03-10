'''
Created on 6 Mar 2015

@author: ademaria
'''
import unittest
from saxsflow.actors.normalisation import Normalisation
from saxsflow.tests.SaxsFlowTestCase import SaxsFlowTestCase


class Test(SaxsFlowTestCase):

    def testRun(self):
        json = self.ispyb.getWorkflowByStatus("PENDING")
        actor = Normalisation(json)

        if len(actor.getDataset().getSubtractionFilePathList()) > 0:
            if len(actor.getDataset().getPDBfilePathList()) > 0:
                actor.run(actor.getDataset().getSubtractionFilePathList()[0], actor.getDataset().getPDBfilePathList()[0], actor.getDataset().getSubtractions(0)["exposureTemperature"])
        pass

if __name__ == "__main__":
    unittest.main()
