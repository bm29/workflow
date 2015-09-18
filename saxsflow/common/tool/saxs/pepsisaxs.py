import os
import subprocess
'''
Created on 9 Mar 2015

@author: ademaria
'''


class PepsiSAXS(object):

    def run(self, outputFolder, pdbs, subtractedFileList):
        os.chdir(outputFolder)

        outputs = []
        summary = []

        header = '%40s%15s%15s%15s%15s' % ('filename', 'Rg prot', 'Rg Hyd Sh', 'Dis. Vol', 'Chi2')
        print header
        summary.append(header)

        for dat in subtractedFileList:
            datBase = os.path.basename(dat)[:-4]
            for pdb in pdbs:
                pdbBase = os.path.basename(pdb)[:-4]
                outputBase = datBase + '_' + pdbBase
                fitName = outputBase + '.fit'
                logName = outputBase + '.log'
                p = subprocess.Popen(['PepsiSAXS', pdb, dat, '-o', fitName, '-au', '2'], stdout = subprocess.PIPE)
                output, err = p.communicate()
                outputs.append(output)
                with open(logName, 'w') as f:
                    f.write(output)
                for l in output.splitlines():
                    if (l.find('Radius of gyration.')>-1) : RgProt = (l.split(':')[1]).split()[0]
                    elif (l.find('Radius of gyration of the hydration shell')>-1) : RgHS = (l.split(':')[1]).split()[0]
                    elif (l.find('Displaced Volume')>-1) : DisVol = (l.split(':')[1]).split()[0]
                    elif (l.find('Chi^2')>-1) : Chi2 = (l.split(':')[1]).split()[0]
                localLog = '%40s%15g%15g%15g%15g' % (logName, float(RgProt), float(RgHS), float(DisVol), float(Chi2))
                print localLog
                summary.append(localLog)

        with open('PepsiSAXS_summary.txt', 'w') as f:
            for line in summary:
                f.write(line + '\n')
