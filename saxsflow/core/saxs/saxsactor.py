'''
Created on 6 Mar 2015

@author: ademaria
'''
import ConfigParser
import os
import datetime
import ntpath
from saxsflow.core.saxs.dataset import SaxsDataset
from saxsflow.common.logger import logger
from saxsflow.common.webservices import ispyb
from saxsflow.common.exception.Exception import SaxsFlowException


class SaxsActor(object):
    '''
    classdocs
    '''
    __xsDataset = None
    __workingFolder = None
    __inputFolder = None
    __outputFolder = None

    def getInputFolderPath(self):
        return self.__inputFolder

    def getOutputFolderPath(self):
        return self.__outputFolder

    def getWorkingFolderPath(self):
        return self.__workingFolder

    def __init__(self, jsonRecord):
        '''
        Constructor
        '''
        self.__xsDataset = SaxsDataset(jsonRecord)

        # Initializing ISPyB
        config = ConfigParser.ConfigParser()
        config.read('../../conf/testing.conf')

        # Connection parameters
        url = config.get('Connection', 'url')
        username = config.get('Connection', 'user')
        password = config.get('Connection', 'password')

        self.ispyb = ispyb.ISPyB(url, username, password)
        # Prepare folder
        self.__prepareFolder()

    def createFolder(self, destination):
        try:
            if not os.path.exists(destination):
                os.makedirs(destination)
            return destination
        except ValueError:
            raise

    def __copyFile(self, ispybFilePath, destination):
        try:
            if not os.path.exists(destination):
                os.makedirs(destination)
            return destination
        except ValueError:
            raise SaxsFlowException(ValueError.message)

    def __prepareFolder(self):
        logger.Logger().log("Preparing folder")
        self.__workingFolder = "/tmp/biosaxsworkflows/" + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        try:
            # Creating working folder
            self.__workingFolder = self.createFolder(self.__workingFolder)
            # Creating input folder
            self.__inputFolder = self.createFolder(self.__workingFolder + "/input")
            # Creating output folder
            self.__outputFolder = self.createFolder(self.__workingFolder + "/output")

            # Downloading subtractions
            for filePath in self.getDataset().getSubtractionFilePathList():
                fileName = ntpath.basename(filePath)
                dest = self.createFolder(self.__inputFolder + "/substraction") + "/" + fileName
                self.ispyb.getFile(filePath, dest)
                self.getDataset().setSubtractedfilePath(filePath, dest)

            for filePath in self.getDataset().getPDBfilePathList():
                fileName = ntpath.basename(filePath)
                dest = self.createFolder(self.__inputFolder + "/pdb") + "/" + fileName
                self.ispyb.getFile(filePath, dest)
                self.getDataset().setPDBfilePath(filePath, dest)

        except ValueError:
            raise SaxsFlowException('My exception occurred, value:', ValueError.value)

    def preProcessing(self):
        logger.Logger().log("preProcessing")
        return

    def run(self):
        logger.Logger().log("run : Method not implemented")
        return

    def postProcessing(self):
        logger.Logger().log("postProcessing: Method not implemented")
        return

    def updateResults(self):
        logger.Logger().log("updateResult: Method not implemented")
        return

    def getDataset(self):
        return self.__xsDataset
