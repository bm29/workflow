'''
Created on 6 Mar 2015

@author: ademaria
'''
from saxsflow.core.saxs.saxsactor import SaxsActor
from subprocess import call
import os


class CrysolActor(SaxsActor):
    '''
    classdocs
    '''
    def run(self, subtractionFilePath, pdbFilePath):
        if subtractionFilePath is not None:
            if pdbFilePath is not None:
                os.chdir(self.outputFolder)
                call(["crysol", pdbFilePath, subtractionFilePath])
