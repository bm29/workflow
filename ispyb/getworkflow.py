import sys
from suds.client import Client
from suds.transport.http import HttpAuthenticated
import os, shutil
from pprint import pprint
import ConfigParser
import json
from dataadapter import *	


def run(**kwargs):
	# Getting first workflow which status is pending (FIFO) 
	response = getWorkflowByStatus("PENDING")

	# Default parameters
	title = ""
	workflowId = None

	# Reading JSON response
	if (json.loads(response)["WORKFLOW"] != ""):
		pendingWorkflow = json.loads(response)
		# Getting workflow and title which is the type of workflow to be routed afterwards
		workflow = (json.loads(pendingWorkflow["WORKFLOW"]))
                title = workflow["workflowTitle"]
	        workflowId = workflow["workflowId"]

		inputParamteres = (json.loads(response)["INPUT"])

		# Subtraction if any
		subtractions = pendingWorkflow["SUBTRACTIONS"]

		# Macromolecules if any
		macromolecules = pendingWorkflow["MACROMOLECULES"]

		return {
			"workflow" 		: workflow,
			"workflowTitle" 	: title.replace(' ', ''),
			"workflowId" 		: workflowId,
			"subtractions" 		: subtractions,
			"macromolecules" 	: macromolecules,
			"workflowStatus" 	: "STARTED",
			"inputParameters" 	: inputParamteres
		}

	return {
		"workflowTitle" 	: None
	}


