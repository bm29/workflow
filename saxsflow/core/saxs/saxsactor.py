'''
Created on 6 Mar 2015

@author: ademaria
'''
import ConfigParser
import os
import datetime
import ntpath
from saxsflow.data.saxsdataset import SaxsDataset
from saxsflow.common.logger import logger
from saxsflow.common.webservices import ispyb


class SaxsActor(object):
    '''
    classdocs
    '''
    xsDataset = None
    workingFolder = None
    inputFolder = None
    outputFolder = None

    def __init__(self, jsonRecord):
        '''
        Constructor
        '''
        self.xsDataset = SaxsDataset(jsonRecord)

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

    def __createFolder(self, destination):
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
            raise

    def __prepareFolder(self):
        logger.Logger().log("Preparing folder")
        self.workingFolder = "/tmp/biosaxsworkflows/" + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        try:
            # Creating working folder
            self.workingFolder = self.__createFolder(self.workingFolder)
            # Creating input folder
            self.inputFolder = self.__createFolder(self.workingFolder + "/input")
            # Creating output folder
            self.outputFolder = self.__createFolder(self.workingFolder + "/output")

            # Downloading subtractions
            i = 0
            for filePath in self.getDataset().getSubtractionFilePathList():
                fileName = ntpath.basename(filePath)
                dest = self.__createFolder(self.inputFolder + "/substraction") + "/" + fileName
                logger.Logger().log("Copying " + filePath + " to " + dest)
                self.ispyb.getFile(filePath, dest)
                self.getDataset().setSubtractedfilePath(filePath, dest)

            i = 0
            for filePath in self.getDataset().getPDBfilePathList():
                fileName = ntpath.basename(filePath)
                dest = self.__createFolder(self.inputFolder + "/pdb") + "/" + fileName
                logger.Logger().log("Copying " + filePath + " to " + dest)
                self.ispyb.getFile(filePath, dest)
                self.getDataset().setPDBfilePath(filePath, dest)

            print(str(self.getDataset().getSubtractionFilePathList()))
            print(str(self.getDataset().getPDBfilePathList()))
        except ValueError:
            print 'My exception occurred, value:', ValueError.value
            raise

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
        return self.xsDataset
