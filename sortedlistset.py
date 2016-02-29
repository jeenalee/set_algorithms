#!/usr/bin/env python
import bench

class SortedListSet(object):
    def __init__(self):
        self.values = []
        
    def insert(self, value):
        index = self.binary_search(value, self.values, 0, len(self.values))
        # index cannot be larger than the len(self.values)
        if index == len(self.values) or value != self.values[index]:
            self.values.insert(index, value)
        
    def contains(self, value):
        index = self.binary_search(value, self.values, 0, len(self.values))
        return index < len(self.values) and value == self.values[index]

    def binary_search(self, value, l, start, end):
        middle = (start + end)/2
        if end == start:
            return middle
        elif l[middle] == value:
            return middle

        # We don't need to consider middle anymore because we ruled it
        # out above. So we recurse with middle +/- 1.
        elif l[middle] < value:
            return self.binary_search(value, l, middle + 1, end)
        elif l[middle] > value:
            return self.binary_search(value, l, start, middle)

        

if __name__ == "__main__":
    print "sortedlistset is the main"
    bench.bench(SortedListSet)
    
    
