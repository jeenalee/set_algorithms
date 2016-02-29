#!/usr/bin/env python

import bench
from collections import namedtuple

Tree = namedtuple('Tree', 'left node right')


def tree_insert(tree, value):
    if not tree:
        return Tree(None, value, None)

    elif value == tree.node:
        return tree

    elif value > tree.node:
        return Tree(tree.left, tree.node, tree_insert(tree.right, value))

    else:
        return Tree(tree_insert(tree.left, value), tree.node, tree.right)

    
def tree_contains(tree, value):
    if not tree:
        return False

    elif value == tree.node:
        return True

    elif value < tree.node:
        return tree_contains(tree.left, value)

    else:
        return tree_contains(tree.right, value)



class UnbalancedTree(object):
    def __init__(self):
        self.tree = None

    def insert(self, value):
        self.tree = tree_insert(self.tree, value)
        
    def contains(self, value):
        return tree_contains(self.tree, value)
   
if __name__ == "__main__":
    print "unbalancedTree is the main"
    bench.bench(UnbalancedTree)
