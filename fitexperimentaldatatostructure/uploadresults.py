import sys
import os, shutil
import json
import ntpath
sys.path.append('/users/opd29/passerelle-edm/scripts/ispyb')
from dataadapter import *	

	
# Tipical destination folder
#	calib_008_sub.dat
#	pdb3v03.pdb
#	pdb3v0300.log
#	pdb3v0300.fit
def run(workingFolder, workflowId, subtractionId, structureId, pdbFile, **kwargs):
	fitFilePath = None
	logFilePath = None
	summaryFilePath = None

	filePathList = os.listdir(workingFolder)	
	for filePath in filePathList:
		if ".fit" in filePath:
			fitFilePath = filePath

		if ".log" in filePath:
			logFilePath = filePath

		if ".txt" in filePath:
			summaryFilePath = filePath
	
	# Upload meta data
	uploadFitStructureToData(workflowId, subtractionId, structureId, summaryFilePath, fitFilePath, logFilePath)	
	# Upload files
	upload(workflowId, workingFolder + "/" + summaryFilePath)
	upload(workflowId, workingFolder + "/" + fitFilePath)
	upload(workflowId, workingFolder + "/" + logFilePath)
	      	

	return {
		"workingFolder"		: workingFolder,
		"filePathList"		: filePathList,
		"workflowId"		: workflowId,
		"pdbFile"		: pdbFile,
		"fitFilePath"		: fitFilePath,
		"logFilePath"		: logFilePath,
		"summaryFilePath"	: summaryFilePath
	}
	
