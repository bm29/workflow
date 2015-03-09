import os
from subprocess import call
'''
Created on 9 Mar 2015

@author: ademaria
'''
from saxsflow.common.exception.Exception import SaxsFlowException


class FFmakerTool(object):
    def run(self, outputFolder, pdbFilePathList):
        try:
            os.chdir(outputFolder)
            call(["ffmaker"] + pdbFilePathList)
        except:
            raise SaxsFlowException()
