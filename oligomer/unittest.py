from runFFmaker import runFFmaker


import os  # datetime, json
# from subprocess import call

pdbFiles = ["/user/around/Link_to_2015/USERS/Abhishek/Manual/Crysol/Ap4A.pdb",
            "/user/around/Link_to_2015/USERS/Abhishek/Manual/Crysol/Ap4A.pdb",
            "/user/around/Link_to_2015/USERS/Abhishek/Manual/Crysol/Ap4A.pdb"]
os.chdir("/user/around/Link_to_2015/USERS/testWorkingFolder")

print pdbFiles
print runFFmaker(pdbFiles).Call_FFmaker()
print FormFactorFile

def gewefjip():
    