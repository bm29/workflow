"""
Read module to obtain scattering data and comments from a dat file 
    
author: Adam Round
Date: 18/02/2015
"""


    
import sys
import os, datetime, json
from subprocess import call
import pdb
from IPython.core.debugger import Pdb


# prepare files and run FFmaker
class runFFmaker:
    def __init__(self, pdbFiles):
        self.pdbFiles = pdbFiles
    
    def Prepare_call_string(self):
        call_string = [""]
        for file in self.pdbFiles:
            pdb = file.replace('/',' ').split()
            call_string.append(pdb[len(pdb) -1 ])
        # Running ff_maker
        print " ".join(call_string)
        #call(["FFmaker", call_string])
        return {"FFmaker_call" : call_string}
            
    def Call_FFmaker(self):
        parameters = ["ffmaker"] + (self.pdbFiles)
        call(parameters)
        print parameters
        