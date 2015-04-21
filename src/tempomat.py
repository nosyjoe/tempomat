#!/usr/bin/env python

import time

from tempvalue import TemperatureValue
from dataset import DataSet
from temp_reader import OneWireTemperatureReader
from file_writer import DataFileWriter

class Tempomat:
    
    def __init__(self):
        self.interval_wait = 2
        self.data_handlers = []
        self.data_handlers.append(DataSet(OneWireTemperatureReader('10-000802d99328'), DataFileWriter('tempds18')))

    def runContinuous(self):
        while True:
            self.runOnce()
            time.sleep(self.interval_wait)

    def runOnce(self):
        for handler in self.data_handlers:
            handler.collect()