#!/usr/bin/env python
import bench

class UnsortedListSet(object):
    def __init__(self):
        self.values = []
        
    def insert(self, value):
        if not self.contains(value):
            self.values.append(value)

    def contains(self, value):
        for x in self.values:
            if x == value:
                return True
        return False

if __name__ == "__main__":
    print "unsortedlistset is the main"
    bench.bench(UnsortedListSet)

    
