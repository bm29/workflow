'''
Created on 6 Mar 2015

@author: ademaria
'''
from saxsflow.core.saxs.saxsactor import SaxsActor
from subprocess import call
import os


class Olygomer(SaxsActor):
    def createFFMakerFolder(self):
        return self.createFolder(self.getOutputFolderPath() + "/FFMaker")

    def createOlygomerFolder(self):
        return self.createFolder(self.getOutputFolderPath() + "/olygomer")

    '''
    classdocs
    '''
    def run(self):
        pdbs = self.getDataset().getPDBfilePathList()
        if pdbs is not None:
            if len(pdbs) > 0:
                ffmakerFolder = self.createFFMakerFolder()
                os.chdir(ffmakerFolder)
                call(["ffmaker"] + pdbs)
                # This should create ff.dat
                formFactorFile = ffmakerFolder + "/ff.dat"
                if os.path.isfile(formFactorFile):
                    if len(self.getDataset().getSubtractionFilePathList()) > 0:
                        os.chdir(self.createOlygomerFolder())
                        call(["oligomer", "/FF", formFactorFile, "/dat", self.getDataset().getSubtractionFilePathList()[0], "/UN", "2", "/cst", "/fit"])
                    else:
                        raise BaseException("Not subtractions found")
                else:
                    raise BaseException("Not form factor file found on " + formFactorFile)

    def updateResults(self):
        return SaxsActor.updateResults(self)
