import os
from subprocess import call
from saxsflow.common.exception.Exception import SaxsFlowException


'''
Created on 9 Mar 2015

@author: ademaria
'''


class Gnom(object):
    outputFolder = None
    defaultOutputGnomFile = "gnom.out"

    def getGnomFile(self):
        if self.outputFolder is not None:
            return self.outputFolder + "/" + self.defaultOutputGnomFile

    def run(self, outputFolder, subtractedFilePath):
        try:
            os.chdir(outputFolder)
            # datgnom %Subtracted File% -o %outputFolder%/gnom.out
            call(["datgnom", subtractedFilePath, "-o", self.defaultOutputGnomFile])
            self.outputFolder = outputFolder
        except:
            raise SaxsFlowException()
