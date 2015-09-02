import sys
import datetime
import os, shutil
from pprint import pprint
import ConfigParser
import urllib
from subprocess import call
import requests 
import json
 
def prepareWorkingFolder():
	workingFolder = "/tmp/biosaxsworkflows/" + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
	if not os.path.exists(workingFolder): 
		os.makedirs(workingFolder)
	return workingFolder

def uploadFiles(workingFolder, urlExtISPyB, fileNames):
	ids = []
	for i in range(len(fileNames)):
		filePath = workingFolder + "/" + fileNames[i]
		if os.path.isfile(filePath):
			url = urlExtISPyB + "/rest/file/filename/" + fileNames[i] + "/upload"
			files = {'file':open(filePath)}
			r = requests.post(url, files=files)
			if r.status_code == 200:
				ids.append({ 'targetId' : r.text, 'name' : fileNames[i], 'value' : fileNames[i], 'type':'file'})
	return ids

def setStatus(projectId, urlExtISPyB, status, runId):
	url = urlExtISPyB + "/rest/{token}/project/" + projectId + "/run/" + runId + "/status/" + status +"/save"
	r = requests.post(url)	

def setFinished(projectId, urlExtISPyB, runId):
	setStatus(projectId, urlExtISPyB, "FINISHED", runId)


def setError(projectId,urlExtISPyB, runId):
	setStatus(projectId, urlExtISPyB, "ERROR", runId)

def run(projectId, runId, subtractionId, pdbFileId, **kwargs):
	startDate = datetime.datetime.now()
	dstPdbFileName = 'pdbFile.pdb'
	dstSubtractedFileName = 'subtraction.dat'

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

	# Example : http://pc593.embl.fr:8080/ispyb-ws/rest/540e26188e608d3b699c077d49acf530a05ecbc8/saxs/opd29/subtraction/26825/download
	token = config.get('Connection', 'token')
	user = config.get('Connection', 'user')
	subtractionUrl = "%s/rest/%s/saxs/%s/subtraction/%s/download" % (urlISPyB, token, user, subtractionId)
	urllib.urlretrieve (subtractionUrl, dstSubtractedFileName)

	# Running crysol
	call(["crysol", "-err", "-cst", dstPdbFileName, dstSubtractedFileName])

	# This produces
	# -rw-r--r-- 1 opd29 jsbg 54232 Jun 29 10:05 pdbFile.pdb
	# -rw-r--r-- 1 opd29 jsbg 57931 Jun 29 10:05 subtraction.dat
	# -rw-r--r-- 1 opd29 jsbg  2967 Jun 29 10:05 pdbFile00.log
	# -rw-r--r-- 1 opd29 jsbg 59641 Jun 29 10:05 pdbFile00.fit
	# -rw-r--r-- 1 opd29 jsbg   248 Jun 29 10:05 crysol_summary.txt
	# Upload Files
	ids = uploadFiles(workingFolder, urlExtISPyB, ["pdbFile00.log", "pdbFile00.fit", "crysol_summary.txt"])
	
	endDate = datetime.datetime.now()
	# Upload results 	
	url = urlExtISPyB + "/rest/{token}/project/" + projectId + "/run/" + runId + "/job/add"
	params = {
			'name': 'Crysol',
			'startDate': startDate,
			'endDate': endDate,
			'version' : 'v2.8.3 (r2962)',
			'output' : json.dumps(ids),
			'status' : 'FINISHED'
	}
	r = requests.post(url, data=params)	

	# Running PepsiSAXS
	call(["PepsiSAXS_0.2", dstPdbFileName, dstSubtractedFileName, "-json"])
	# This produces
	#-rw-r--r-- 1 opd29 jsbg    6633 Jul  8 16:07 pdbFile.log
	#-rw-r--r-- 1 opd29 jsbg   76208 Jul  8 16:07 pdbFile.fit
	ids = uploadFiles(workingFolder, urlExtISPyB, ["pdbFile.log", "pdbFile.fit"])
	params = {
			'name': 'PepsiSAXS',
			'startDate': startDate,
			'endDate': endDate,
			'version' : 'v0.1',
			'output' : json.dumps(ids),
			'status' : 'FINISHED'
	}
	r = requests.post(url, data=params)	


	if r.status_code == 200:
		setFinished(projectId, urlExtISPyB, runId)
	else:
		setError(projectId, urlExtISPyB, runId)
	

	return {"Output": filePdbUrl,"projectId": projectId,"runId": runId,"subtractionId": subtractionId,"pdbFileId": pdbFileId}
