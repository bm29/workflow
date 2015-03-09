'''
Created on 6 Mar 2015

@author: ademaria
'''
import os
from saxsflow.core.saxs.saxsactor import SaxsActor
from subprocess import call
from saxsflow.common.exception.Exception import SaxsFlowException
from saxsflow.common.tool.ffmaker import FFmakerTool
import saxsflow
from saxsflow.common.tool import oligomer


class Oligomer(SaxsActor):
    def createFFMakerFolder(self):
        return self.createFolder(self.getOutputFolderPath() + "/FFMaker")

    def createOligomerFolder(self):
        return self.createFolder(self.getOutputFolderPath() + "/Oligomer")

    '''
    classdocs
    '''
    def run(self):
        pdbs = self.getDataset().getPDBfilePathList()
        if pdbs is not None:
            if len(pdbs) > 0:
                ffmakerFolder = self.createFFMakerFolder()
                # Run ffmaker
                FFmakerTool().run(ffmakerFolder, pdbs)
                # This should create ff.dat
                formFactorFile = ffmakerFolder + "/ff.dat"

                if os.path.isfile(formFactorFile):
                    if len(self.getDataset().getSubtractionFilePathList()) > 0:
                        oligomerOutputFolder = self.createOligomerFolder()
                        subtractedFilePath = self.getDataset().getSubtractionFilePathList()[0]
                        oligomer.Oligomer().run(oligomerOutputFolder, formFactorFile, subtractedFilePath)

                        # os.chdir(self.createOligomerFolder())
                        # subtractedFilePath = self.getDataset().getSubtractionFilePathList()[0]
                        # call(["oligomer", "/FF", formFactorFile, "/dat", subtractedFilePath, "/UN", "2", "/cst", "/fit"])
                    else:
                        raise SaxsFlowException("Not subtractions found")
                else:
                    raise SaxsFlowException("Not form factor file found on " + formFactorFile)

    def updateResults(self):
        return SaxsActor.updateResults(self)
