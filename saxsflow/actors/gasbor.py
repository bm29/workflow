'''
Created on 9 Mar 2015

@author: ademaria
'''
from saxsflow.core.saxs.saxsactor import SaxsActor
from saxsflow.common.tool import gnom
from saxsflow.common.tool import gasbor
import os


class Gasbor(SaxsActor):
    def createGasborFolder(self):
        return self.createFolder(self.getOutputFolderPath() + "/gasbor")

    def createGnomFolder(self):
        return self.createFolder(self.getOutputFolderPath() + "/gnom")

    def run(self):
        if self.getDataset().getSubtractionFilePathList() is not None:
            if len(self.getDataset().getSubtractionFilePathList()) > 0:
                subtractedFilePath = self.getDataset().getSubtractionFilePathList()[0]
                gnomTool = gnom.Gnom()
                gnomTool.run(self.createGnomFolder(), subtractedFilePath)
                if os.path.isfile(gnomTool.getGnomFile()):
                    gasbor.Gasbor().run(self.createGasborFolder(), gnomTool.getGnomFile())
