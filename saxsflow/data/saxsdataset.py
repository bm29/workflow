import json


class SaxsDataset(object):
    '''
    Biosaxs Dataset
    '''
    json = None

    def __init__(self, jsonRecord):
        self.json = json.loads(jsonRecord)

    def getInput(self, i=None):
        if i is None:
            return self.json["INPUT"]
        else:
            return self.json["INPUT"][i]

    def getSubtractions(self, i=None):
        if i is None:
            return self.json["SUBTRACTIONS"]
        else:
            return self.json["SUBTRACTIONS"][i]

    def getSubtractionFilePathList(self):
        subtractions = self.getSubtractions()
        filePath = []
        for i in range(len(subtractions)):
            filePath.append(subtractions[i]["substractedFilePath"])
        return filePath

    def getMacromolecules(self, i=None):
        if i is None:
            return self.json["MACROMOLECULES"]
        else:
            return self.json["MACROMOLECULES"][i]

    def getPDBfilePathList(self, i=None):
        macromolecules = self.getMacromolecules()
        filePath = []
        for i in range(len(macromolecules)):
            for j in range(len(macromolecules[i]["structure3VOs"])):
                structure = macromolecules[i]["structure3VOs"][j]
                if structure["structureType"] == "PDB":
                    filePath.append(structure["filePath"])
        return filePath

    def setSubtractedfilePath(self, currentFilePath, workingFolderFilePath):
        subtractions = self.getSubtractions()
        for i in range(len(subtractions)):
            if (subtractions[i]["substractedFilePath"]) == currentFilePath:
                subtractions[i]["substractedFilePath"] = workingFolderFilePath

    def setPDBfilePath(self, currentFilePath, workingFolderFilePath):
        macromolecules = self.getMacromolecules()
        for i in range(len(macromolecules)):
            for j in range(len(macromolecules[i]["structure3VOs"])):
                structure = macromolecules[i]["structure3VOs"][j]
                if structure["filePath"] == currentFilePath:
                    structure["filePath"] = workingFolderFilePath
