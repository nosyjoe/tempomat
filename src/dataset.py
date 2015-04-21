#!/usr/bin/env python

class DataSet:
    
    def __init__(self, data_reader, data_writer = None):
        self.reader = data_reader
        self.writer = data_writer
        self.latest = []
        
    def collect(self):
        value = self.reader.read_value()
        was_added = self.add(value)
        
        print value
        
        # write value if it was accepted
        if was_added and self.writer:
            self.writer.append(value)

    def add(self, value):
        oldOldValue = None
        oldValue = None
        if len(self.latest) > 1:
            oldOldValue = self.latest[1]
        if len(self.latest) > 0:
            oldValue = self.latest[0]
        
        if not oldValue or value != oldValue:
            if not oldOldValue or value != oldOldValue:
                self.latest = [value] + self.latest[:10]
                return True
                
        return False
