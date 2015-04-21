#!/usr/bin/env python

from datetime import date

class DataFileWriter:
    
    def __init__(self, filename_base):
        self.filename_base = filename_base
        
    def get_filename(self):
        return self.filename_base +"_" + date.today().strftime("%Y-%m-%d") + ".csv"
    
    def append(self, value):
        with open(self.get_filename(), 'a+') as outfile:
            print>>outfile, str(value)