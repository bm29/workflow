"""
 module to obtain FormFactor file from input PDB's to be used as input for oligomer 
    
author: Adam Round
Date: 23/02/2015
"""


import os, datetime
from subprocess import call

def run(workingFolder, subtractionFile, FormFactorFile, subtractionId, structureId,  **kwargs):
    # Creating folder
    subworkingFolder = workingFolder +"/oligomer_" + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    if not os.path.exists(subworkingFolder): 
        os.makedirs(subworkingFolder)
    os.chdir(subworkingFolder)
    # Running crysol
    call(["oligomer", "/FF", FormFactorFile, "/dat", subtractionFile, "/UN", "2", "/cst", "/fit", "oligomer"])
    return {
        "workingFolder"        : workingFolder,
        "FormFactorFile"        : FormFactorFile,
        "subtractionFile"    : subtractionFile,
        "structureId"        : structureId,
        "subtractionId"        : subtractionId
    }
