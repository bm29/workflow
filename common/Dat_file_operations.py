"""
Perform operations on scattering data from a Dat file 
    
author: Adam Round
Date: 18/02/2015
"""

from Dat_file_scattering_reader import Dat_file_scattering_reader 
    
class Dat_file_operations:
    
    my_reader = None
    
    def __init__(self, filename):
        self.sub_filename = filename
        self.my_reader = Dat_file_scattering_reader(filename)
        
    def get_data(self, s_min, s_max):
        data =  self.my_reader.get_data()
        data_range = []
        for line in data:
            column1 = line.split()[0]
            if float(column1) >= s_min and float(column1) <= s_max:
                data_range.append(line)
        return data_range
        
        
        
    def Average_scatering_intensity(self,s_min, s_max):
        data_range = self.get_data(s_min, s_max)
        #total scattering intensity
        total_int = 0
        for line in data_range:
            intensity = line.split()[1]
            total_int = total_int + float(intensity)

        return {"Average_Intensity" : (total_int / len(data_range))}
            