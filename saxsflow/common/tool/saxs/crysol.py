import os
from subprocess import call
from saxsflow.common.exception.Exception import SaxsFlowException


'''
Created on 9 Mar 2015

@author: ademaria
'''


class Crysol(object):

    def run(self, outputFolder, pdb, subtractedFilePath):
        try:
            os.chdir(outputFolder)
            call(["crysol", pdb, subtractedFilePath])
        except ValueError:
            raise SaxsFlowException(ValueError)
