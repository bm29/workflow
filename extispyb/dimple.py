import sys
import datetime
import os, shutil
from pprint import pprint
import ConfigParser
import urllib
from subprocess import call
import requests 
import json
import ntpath

import sys
sys.path.append("/opt/pxsoft/EDNA/vMX/edna/kernel/src")
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

EDFactoryPluginStatic.loadModule("XSDataCCP4v1_0")
from XSDataCCP4v1_0 import XSDataInputDimple


 
def prepareWorkingFolder():
	workingFolder = "/tmp/biosaxsworkflows/" + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
	if not os.path.exists(workingFolder): 
		os.makedirs(workingFolder)
	return workingFolder



def setStatus(projectId, urlExtISPyB, status, runId):
	url = urlExtISPyB + "/rest/{token}/project/" + projectId + "/run/" + runId + "/status/" + status +"/save"
	r = requests.post(url)	

def setFinished(projectId, urlExtISPyB, runId):
	setStatus(projectId, urlExtISPyB, "FINISHED", runId)


def setError(projectId,urlExtISPyB, runId):
	setStatus(projectId, urlExtISPyB, "ERROR", runId)

def runDimple(projectId,urlExtISPyB, runId):
	setStatus(projectId, urlExtISPyB, "ERROR", runId)

def uploadFile(urlExtISPyB, filePath, fileType):
	if os.path.isfile(filePath):
		url = urlExtISPyB + "/rest/file/filename/" + ntpath.basename(filePath) + "/upload"
		files = {'file':open(filePath)}
		r = requests.post(url, files=files)
		if r.status_code == 200:
			return ({ 'targetId' : r.text, 'name' : ntpath.basename(filePath), 'value' : ntpath.basename(filePath), 'type':fileType})
	return None

def run(token, projectId, runId, pdbFileId, mtzFileId, **kwargs):
	startDate = datetime.datetime.now()
	dstPdbFileName = 'pdbFile.pdb'
	dstMtzFileName = 'mtz.mtz'

	# Config file
	config = ConfigParser.ConfigParser()
	config.read('/users/opd29/passerelle-edm/scripts/extispyb/extispyb.properties')

	# Connection parameters
	urlExtISPyB = config.get('Connection', 'urlExtISPyB')
	urlISPyB = config.get('Connection', 'urlISPyB')

	# Creating Working folder
	workingFolder = prepareWorkingFolder()

	# Getting PDB input
	os.chdir(workingFolder)
	filePdbUrl = "%s/rest/file/%s/download" % (urlExtISPyB, pdbFileId)
	urllib.urlretrieve (filePdbUrl, dstPdbFileName)

	# Getting MTZ input
	fileMtzUrl = "%s/rest/file/%s/download" % (urlExtISPyB, mtzFileId)
	urllib.urlretrieve (fileMtzUrl, dstMtzFileName)

	xsDataInputDimple = XSDataInputDimple()
	xsDataInputDimple.mtz = XSDataFile(XSDataString(workingFolder + "/" + dstMtzFileName))
	xsDataInputDimple.pdb = XSDataFile(XSDataString(workingFolder + "/" + dstPdbFileName))

	edPluginExecDimple = EDFactoryPluginStatic.loadPlugin("EDPluginExecDimplev1_0")
	edPluginExecDimple.dataInput = xsDataInputDimple
	edPluginExecDimple.executeSynchronous()
	
	# Uploading files
	ids = []
	for i in range(len(edPluginExecDimple.dataOutput.getBlob())):
		ids.append(uploadFile(urlExtISPyB, edPluginExecDimple.dataOutput.getBlob()[i].getPath().getValue(), "blob"))
	
	ids.append(uploadFile(urlExtISPyB, edPluginExecDimple.dataOutput.getFinalMtz().getPath().getValue(), "finalMtz"))
	ids.append(uploadFile(urlExtISPyB, edPluginExecDimple.dataOutput.getFinalPdb().getPath().getValue(), "finalPdb"))
	ids.append(uploadFile(urlExtISPyB, edPluginExecDimple.dataOutput.getLog().getPath().getValue(), "log"))
	ids.append(uploadFile(urlExtISPyB, edPluginExecDimple.dataOutput.getFindBlobsLog().getPath().getValue(), "findBlobsLog"))
	ids.append(uploadFile(urlExtISPyB, edPluginExecDimple.dataOutput.getRefmac5restrLog().getPath().getValue(), "refmac5restrLog"))

	#ids = uploadFiles(urlExtISPyB, files)
	
	# Upload results 	
	url = urlExtISPyB + "/rest/{token}/project/" + projectId + "/run/" + runId + "/job/add"
	params = {
			'name': 'Dimple',
			'startDate': startDate,
			'endDate':  datetime.datetime.now(),
			'version' : 'v2.8.3 (r2962)',
			'output' : json.dumps(ids),
			'status' : 'FINISHED'
	}

	r = requests.post(url, data=params)	

	if r.status_code == 200:
		setFinished(projectId, urlExtISPyB, runId)
	else:
		setError(projectId, urlExtISPyB, runId)
	return {"ids" :  ids, "Output": edPluginExecDimple.dataOutput.marshal(), "dstMtzFileName": dstMtzFileName,  "dstPdbFileName": dstPdbFileName}
