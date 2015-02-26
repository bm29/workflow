"""
 module to obtain FormFactor file from input PDB's to be used as input for oligomer 
    
author: Adam Round
Date: 23/02/2015
"""

import os, datetime
from subprocess import call

def run(workingFolder, subtractionFile, pdbFiles, subtractionId, structureId,  **kwargs):
    # Creating folder
    subworkingFolder = workingFolder +"/ffmaker_" + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    if not os.path.exists(subworkingFolder): 
        os.makedirs(subworkingFolder)
    os.chdir(subworkingFolder)

    # Running ffmaker
    call(["ffmaker"] + (pdbFiles))
    
    FormFactorFile = [subworkingFolder + "FF.dat"]
    
    return {
        "workingFolder"         : workingFolder,
        "FormFactorFile"        : FormFactorFile,
        "structureId"           : structureId,
        "subtractionId"         : subtractionId
    }
