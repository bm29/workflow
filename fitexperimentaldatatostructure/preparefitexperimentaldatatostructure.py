import sys
import os, shutil
import json
import ntpath

sys.path.append('/users/opd29/passerelle-edm/scripts/ispyb')
from dataadapter import *	


def getSubtractionFilePath(subtractions):
	filePathList = []
	if subtractions is not None:
		# Converting to dict
		dict = json.loads(subtractions)
		for i in range(0, len(dict)):
			filePathList.append(dict[i]["substractedFilePath"])
	return filePathList				



def getLocalFilepath(filepathList):
	localfilepathList = []
	for filePath in filepathList:
		if filePath is not None:		
			localfilepathList.append(filePath)
	return localfilepathList
	

# Given n macomolecule it will return an array with the pdb files pointing to the local file system
def getPdbFilePath(jsonMacromolecule):
	pdbs = []
	macromolecules = json.loads(jsonMacromolecule)
	for i in range(0, len(macromolecules)):
			macromolecule = macromolecules[i]
			structures = (macromolecule["structure3VOs"])
			for j in range(0, len(structures)):
				filePath =  structures[j]["filePath"]
				if filePath is not None:
					pdbs.append(structures[j]["filePath"])
					
				
	return pdbs



def getSubtractionId(subtractions):
	filePathList = []
	if subtractions is not None:
		# Converting to dict
		dict = json.loads(subtractions)
		for i in range(0, len(dict)):
			return dict[i]["subtractionId"]


def getStructureId(inputParameters):
	
	params = json.loads(inputParameters)
	for i in range(0, len(params)):
			param = params[i]["name"]
			if param == "structureId":
				return  params[i]["value"]
				
#	return pdbs

def run(workingFolder, subtractions, macromolecules, inputParameters, **kwargs):
	#
	structureId = getStructureId(inputParameters)

	# List of subtraction files
	filepathList = getSubtractionFilePath(subtractions)
	for filePath in filepathList:
		fileName = ntpath.basename(filePath)
		dest = str(workingFolder) + "/" + fileName
		getFile(filePath, dest)
		subtractionFile = dest

	# Gettig pdb filePath of the pdb
	pdbLocalfilepathList = getPdbFilePath(macromolecules)
	pdbs = []
	for filePath in pdbLocalfilepathList:
		fileName = ntpath.basename(filePath)
		dest = str(workingFolder) + "/" + fileName
		getFile(filePath, dest)
		pdbFile = dest
		pdbs.append(pdbFile)

	
	subtractionId = getSubtractionId(subtractions)
	return {
		"subtractionFilePathList"	: [subtractionFile],
		"pdbFile"			: pdbFile,
		"pdbs"				: pdbs,
		"structureId"			: structureId,
		"subtractionId"			: subtractionId
	}
	
