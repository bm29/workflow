import sys
from suds.client import Client
from suds.transport.http import HttpAuthenticated
import os, shutil
from pprint import pprint
import ConfigParser
import json
from dataadapter import *	

def run(workflowId, workflowStatus, **kwargs):
	setWorkFlowStatus(workflowId, workflowStatus)
	return {
		"workflowId" : workflowId,
		"workflowStatus" : workflowStatus
	}	
