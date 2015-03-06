import sys
import os, datetime, json
from subprocess import call

def run(workingFolder, subtractionFile, pdbFile, subtractionId, structureId,  **kwargs):
	# Creating folder
	os.chdir(workingFolder)
	# Running crysol
	call(["crysol", "-err", "-cst", pdbFile, subtractionFile])
	return {
		"workingFolder"		: workingFolder,
		"pdbFile"			: pdbFile,
		"subtractionFile"	: subtractionFile,
		"structureId"		: structureId,
		"subtractionId"		: subtractionId
	}
	
