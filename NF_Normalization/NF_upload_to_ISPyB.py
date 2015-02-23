import sys
sys.path.append('/users/opd29/passerelle-edm/scripts/ispyb')
from dataadapter import *

def run(workflowId, results, ScaledNF, AbsoluteNF, **kwargs):
    
    # Upload meta data
    uploadNFcheck(workflowId, results, ScaledNF, AbsoluteNF)  
   
    return {}