import sys
sys.path.append('/users/opd29/passerelle-edm/scripts/ispyb')
from dataadapter import *


def UploadToISPyB(workflowId, results, ScaledNF, AbsoluteNF, **kwargs):

    # Upload meta data
    upload(workflowId, results, ScaledNF, AbsoluteNF)

    return {}
