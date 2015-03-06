'''
Created on 6 Mar 2015

@author: ademaria
'''
from saxsflow.core.saxs.saxsactor import SaxsActor
from saxsflow.common.file.scatteringfile import ScatteringFile
from saxsflow.common.math.normalisationfactorcalculator import NormalisationFactorCalculator


class NormalisationActor(SaxsActor):
    '''
    classdocs
    '''
    def run(self, subtractionFilePath, pdbFilePath, exposoreTemperature):
        sensitivity = 2
        temp_measured = float(exposoreTemperature)
        current_NF = 0.007381988
        # must be updated to get the real value suggested code below
        # current_NF = float(subtractions_array[0]["normalisationFactor"])
        H2O_sub = subtractionFilePath

        I0_m = ScatteringFile(H2O_sub).Average_scatering_intensity(0.35, 0.45)["Average_Intensity"]

        print(str(NormalisationFactorCalculator().Check_NF(temp_measured, current_NF, float(I0_m), sensitivity)))

    def updateResults(self):
        # self.ispyb.uploadNFcheck(workflowId, results, ScaledNF, AbsoluteNF)
        pass
