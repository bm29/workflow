'''
Created on 9 Mar 2015

@author: ademaria
'''
from saxsflow.core.saxs.saxsactor import SaxsActor
from saxsflow.common.tool.saxs.pepsisaxs import PepsiSAXS
from saxsflow.common.tool.saxs import pepsisaxs


class PepsiSAXS(SaxsActor):
    def run(self):
        if self.getDataset().getSubtractionFilePathList() is not None:
            if len(self.getDataset().getSubtractionFilePathList()) > 0:
                
                tool = pepsisaxs.PepsiSAXS()
                tool.run(self.getOutputFolderPath(), self.getDataset().getPDBfilePathList(), self.getDataset().getSubtractionFilePathList())
