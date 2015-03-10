'''
Created on 9 Mar 2015

@author: ademaria
'''
import unittest
import ConfigParser
from saxsflow.common.webservices import ispyb


class SaxsFlowTestCase(unittest.TestCase):
    ispyb = None

    def setUp(self):
        print("Setup client")
        # Reading configuration params
        try:
            config = ConfigParser.ConfigParser()
            config.read('../../conf/testing.conf')
            # Connection parameters
            url = config.get('Connection', 'url')
            username = config.get('Connection', 'user')
            password = config.get('Connection', 'password')
            print(str(url))
            self.ispyb = ispyb.ISPyB(url, username, password)
            self.json = self.ispyb.getWorkflowByStatus("PENDING")
        except:
            self.json = '{"SUBTRACTIONS":[{"total":"0.562219614687","sourceFilePath":"/data/pyarch/bm29/opd29/4792/BSA.xml","measurementCode":"bsa","I0":"110.922352941","abinitioCount":0,"superposisitionCount":0,"flow":true,"volumeToLoad":"50","framesCount":"10","fitCount":0,"I0Stdev":"0.0853229411765","specimenId":33904,"averageFilePath":" /data/pyarch/bm29/opd29/4792/1d/calib_009_ave.dat","kratkyFilePath":"/data/pyarch/bm29/opd29/4792/1d/calib_008_sub-Kratky.png","creationTime":"Sep 26, 2014 11:49:27 AM","rgStdev":"0.0220899","proposalId":10,"volumePorod":"125.251","gnomFilePathOutput":" /data/pyarch/bm29/opd29/4792/1d/calib_008_sub.out","rgGuinier":"3.29914","status":"FINISHED","firstPointUsed":"22","code":"","transmission":"100.0","rigidbodyCount":0,"sessionId":38019,"bufferAcronym":"","quality":"0.868335","measurementToDataCollectionId":81528,"dmax":"11.54699","isagregated":"False","waitTime":"0.0","bufferId":637,"dataCollectionOrder":3,"rg":"3.29914","exposureTemperature":"20.0","runId":41306,"subtractionId":18734,"lastPointUsed":"55","framesMerge":"10","scatteringFilePath":"/data/pyarch/bm29/opd29/4792/1d/calib_008_sub-scattering.png","name":"BSA.xml","gnomFilePath":"/data/pyarch/bm29/opd29/4792/1d/calib_008_sub-density.png","guinierFilePath":"/data/pyarch/bm29/opd29/4792/1d/calib_008_sub-Guinier.png","concentration":"0.0","experimentId":4792,"frameListId":49461,"acronym":"","experimentType":"CALIBRATION","samplePlatePositionId":32589,"priorityLevelId":3,"dataCollectionId":27176,"creationDate":"Sep 26, 2014 11:45:33 AM","mergeId":45253,"extraFlowTime":"10","viscosity":"Low","measurementId":81528,"rgGnom":"3.31269418847","volume":"50","substractedFilePath":" /data/pyarch/bm29/opd29/4792/1d/calib_008_sub.dat","comments":"[BsxCube] Generated from BsxCube"}],"INPUT":[{"value":"18734","name":"subtractionId"},{"value":"10","name":"structureId"}],"WORKFLOW":"{\"workflowId\":11273,\"workflowTitle\":\"FitExperimentalDatatoStructure\",\"workflowType\":\"BioSAXS Post Processing\",\"comments\":\"FitExperimentalDatatoStructure run from ISPyB for subtractionId: undefined and structureId 10\",\"status\":\"PENDING\",\"recordTimeStamp\":\"Jan 21, 2015 6:52:56 PM\",\"proposalId\":10}","MACROMOLECULES":[{"macromoleculeId":1,"proposalId":10,"name":"bsa","acronym":"bsa","molecularMass":"","extintionCoefficient":"","comments":"","structure3VOs":[{"structureId":10,"macromoleculeId":1,"filePath":"/data/pyapdb/opd29/4F5S.pdb","name":"4F5S.pdb","structureType":"PDB","creationDate":"Jan 21, 2015 12:00:00 AM"}],"stoichiometry":[]}]}'
        pass

    def tearDown(self):
        pass
