#
#    Project: BioSaxs
#
#    Copyright (C) EMBL
#
#    Authors:
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from suds.client import Client
from suds.transport.http import HttpAuthenticated
import base64
import ntpath


class ISPyB(object):
    '''
    Python Interface to use ISPyB WebServices
    '''
# configuration_file_path = '/users/opd29/passerelle-edm/scripts/ispyb/ispyb.properties'

    def __init__(self, url, username, password):
        httpAuthenticatedToolsForAutoprocessingWebService = HttpAuthenticated(username=username, password=password)
        self.client = Client(url, transport=httpAuthenticatedToolsForAutoprocessingWebService, cache=None, timeout=15)

    def getClient(self):
        return self.client
    '''
    Status: PENDING, STARTED, FINISHED, ERROR
    '''
    def getWorkflowByStatus(self, status):
        return self.getClient().service.getWorkflowByStatus(status)
    '''
    Download a file from ISPyB and copies into the destionation folder
    '''
    def getFile(self, filepath, destination):
        downloaded_bytes = self.getClient().service.getFile(filepath)
        if downloaded_bytes is not None:
            bytes64 = base64.decodestring(downloaded_bytes)
            newFile = open(destination, "wb")
            newFile.write(bytes64)
            print("Writting to " + destination)
    '''
    Upload a file to ISPyB
    '''
    def upload(self, workflowId, filePath):
        uploaded_bytes = open(filePath, "rb").read()
        bytes64 = base64.b64encode(uploaded_bytes)
        fileName = ntpath.basename(filePath)
        self.getClient().service.upload(workflowId, fileName, bytes64)

    def uploadFitStructureToData(self, workflowId, subtractionId, structureId, summaryFilePath, fitFilePath, logFilePath):
        self.getClient().service.uploadFitStructureToData(workflowId, subtractionId, structureId, summaryFilePath, fitFilePath, logFilePath)

    def uploadNFcheck(self, workflowId, results, ScaledNF, AbsoluteNF):
        self.getClient().service.uploadNFcheck(workflowId, results, ScaledNF, AbsoluteNF)
