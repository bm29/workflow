'''
Created on 9 Mar 2015

@author: ademaria
'''
from saxsflow.core.saxs.saxsactor import SaxsActor
from saxsflow.common.tool.saxs import gnom


class Gnom(SaxsActor):
    def run(self):
        if self.getDataset().getSubtractionFilePathList() is not None:
            if len(self.getDataset().getSubtractionFilePathList()) > 0:
                subtractedFilePath = self.getDataset().getSubtractionFilePathList()[0]
                gnom.Gnom().run(self.getOutputFolderPath(), subtractedFilePath)
