import sys
import os, datetime

def run(**kwargs):
	workingFolder = "/tmp/biosaxsworkflows/" + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
	if not os.path.exists(workingFolder): 
		os.makedirs(workingFolder)

	return {
		"workingFolder"		: workingFolder
	}
	
