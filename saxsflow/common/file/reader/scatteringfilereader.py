"""
Read module to obtain scattering data and comments from a dat file 
    
author: Adam Round
Date: 18/02/2015
"""

import re

# Calculate the average scattering intensity within a chosen s range
class ScatteringFileReader:
    
    def __init__(self, sub_filename):
        self.sub_filename = sub_filename
        self.data = None
        self.comments = None
        #self.s_min = s_min
        #self.s_max = s_max
        
    def __isFloat(self, value):
        return re.match("\-?\d+\.\d+e[\-|\+]\d+", value)
    
    def __isDataLine(self, line):
        if len(line.split()) == 3: #and type(line.split()[0]) is float and type(line.split()[1]) is float and type(line.split()[2]) is float :
            column1, column2, column3 = line.split()
            if (self.__isFloat(column1) and self.__isFloat(column2) and self.__isFloat(column3)):
            #    if float(column1) >= s_min and float(column1) <= s_max:
                return True
        return False
    
    #def read(self, s_min, s_max):
    def __read(self):
        self.data = []
        self.comments = []
        with open(self.sub_filename,"r") as dat:
            for line in dat:
                if self.__isDataLine(line):
                    self.data.append(line)
                else:
                    self.comments.append(line)

                        
    def get_data(self):
        if self.data is None:
            self.__read() 
        return self.data   
    
    def get_coments(self):
        if self.comments is None:
            self.__read() 
        return self.comments  