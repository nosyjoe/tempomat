#!/usr/bin/env python

import re
import os
from tempvalue import TemperatureValue

class OneWireTemperatureReader:

    tempre = re.compile('.*t=(\d+)')
    
    def __init__(self, device_id):
        self.device_id = device_id
        # self.data_file = os.path.join('/sys/bus/w1/devices', self.device_id, 'w1_slave')
        self.data_file = os.path.join('/Users/philipp/Documents/dev/making/temp-o-mat/src', self.device_id, 'w1_slave')
        
    def read_value(self):
        # with open('w1_slave') as f:
        with open(self.data_file) as f:
            for line in f:
                match = self.tempre.match(line)
                if match:
                    return TemperatureValue(float(match.group(1)) / 1000.)
            