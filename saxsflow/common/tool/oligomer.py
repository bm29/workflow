import os
from subprocess import call
'''
Created on 9 Mar 2015

@author: ademaria
'''
from saxsflow.common.exception.Exception import SaxsFlowException


class Oligomer(object):
    def run(self, outputFolder, formFactorFile, subtractedFilePath):
        try:
            os.chdir(outputFolder)
            call(["oligomer", "/FF", formFactorFile, "/dat", subtractedFilePath, "/UN", "2", "/cst", "/fit"])
        except:
            raise SaxsFlowException()
