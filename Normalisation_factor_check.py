"""
Actor to check normalisation of water scattering in passerelle workflow
    
author: Adam Round
Date: 20/02/2015
"""
import json

from normalisation_factor_calculator import Normalisation_Factor_Calculator
from Dat_file_operations import Dat_file_operations



def run (subtractions, subtractionFilePathList, **kwargs):
    subtractions_array = json.loads(subtractions)
    # extract required parameters from subtractions
    sensitivity = 2
    temp_measured = float(subtractions_array[0]["exposureTemperature"])
    current_NF = 0.007381988
    H2O_sub = json.loads(subtractionFilePathList)[0]
    
    I0_m = Dat_file_operations(H2O_sub).Average_scatering_intensity(0.35, 0.45)["Average_Intensity"]
    
    return Normalisation_Factor_Calculator().Check_NF(temp_measured, current_NF, float(I0_m), sensitivity)
    