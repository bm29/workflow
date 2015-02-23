import sys
import os, shutil
import json
import ntpath
sys.path.append('/users/opd29/passerelle-edm/scripts/ispyb')
from dataadapter import *	





def run(subtractions, macromolecules, **kwargs):
	return {

		subtractions : subtractions,
		macromolecules : macromolecules
	}
