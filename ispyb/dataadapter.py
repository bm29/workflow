import sys
from suds.client import Client
from suds.transport.http import HttpAuthenticated
import os, shutil
from pprint import pprint
import ConfigParser
import json
import base64
import ntpath

def getClient():
	# Config file
	config = ConfigParser.ConfigParser()
	config.read('/users/opd29/passerelle-edm/scripts/ispyb/ispyb.properties')

	# Connection parameters
	url = config.get('Connection', 'url')
	username = config.get('Connection', 'user')
	password = config.get('Connection', 'password')

	# Authentication
	httpAuthenticatedToolsForAutoprocessingWebService = HttpAuthenticated(username = username, password = password ) 
	return Client( url, transport = httpAuthenticatedToolsForAutoprocessingWebService, cache = None, timeout = 15 )

def getWorkflowByStatus(status):
        return getClient().service.getWorkflowByStatus(status)

def setWorkFlowStatus(workflowId, status):
	getClient().service.setWorkFlowStatus(workflowId, status)
	#getClient().service.setWorkFlowStatus(workflowId, "PENDING")

def getFile(filepath, destination):
	bytes = getClient().service.getFile(filepath)
	if bytes is not None:
		bytes64 = base64.decodestring(bytes)	
		newFile = open (destination, "wb")
		newFile.write(bytes64)
	
def upload(workflowId, filePath):
	bytes = open(filePath, "rb").read()
	bytes64 = base64.b64encode(bytes)	
	fileName = ntpath.basename(filePath)
	getClient().service.upload(workflowId, fileName, bytes64)


def uploadFitStructureToData(workflowId, subtractionId, structureId, summaryFilePath, fitFilePath, logFilePath):
	getClient().service.uploadFitStructureToData(workflowId, subtractionId, structureId, summaryFilePath, fitFilePath, logFilePath)
