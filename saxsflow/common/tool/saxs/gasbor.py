import os
import traceback
import ntpath
import shutil
from subprocess import call
from saxsflow.common.exception.Exception import SaxsFlowException


'''
Created on 9 Mar 2015

@author: ademaria
'''


class Gasbor(object):
    outputFolder = None
    maximumNumberResidues = "10"

    def run(self, outputFolder, gnomFile):
        try:
            print(str(gnomFile))
            shutil.copy(gnomFile, outputFolder)
            os.chdir(outputFolder)
            call(["gasbori", ntpath.basename(gnomFile), self.maximumNumberResidues])
        except ValueError:
            traceback.print_exc()
            raise SaxsFlowException(ValueError.message)
