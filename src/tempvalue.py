#!/usr/bin/env python

import time

class TemperatureValue:
    
    def __init__(self, value_in_degrees):
        self.value = value_in_degrees
        self.timestamp = time.localtime()
        
    def __cmp__(self, other):
        if self.value < other.get_value():
            return -1
        elif self.value > other.get_value():
            return 1
        else: 
            return 0
        
    def get_value(self):
        return self.value
        
    def __str__(self):
        return "{0} {1}".format(time.strftime("\"%Y-%m-%d %H:%M:%S\"", self.timestamp), self.value)
