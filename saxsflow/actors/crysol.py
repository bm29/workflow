'''
Created on 6 Mar 2015

@author: ademaria
'''
import os
from saxsflow.core.saxs.saxsactor import SaxsActor
from saxsflow.common.tool import crysol


class Crysol(SaxsActor):

    def run(self, subtractionFilePath, pdbFilePath):
        if subtractionFilePath is not None:
            if pdbFilePath is not None:
                os.chdir(self.getOutputFolderPath())
                for i in range(len(self.getDataset().getSubtractionFilePathList())):
                    crysol.Crysol().run(self.getOutputFolderPath(), self.getDataset().getPDBfilePathList()[0], self.getDataset().getSubtractionFilePathList()[i])
