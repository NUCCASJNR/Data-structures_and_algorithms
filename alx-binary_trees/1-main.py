#!/usr/bin/python3

LeftNode = __import__('1-binary_tree_insert_left').LeftNode

root = LeftNode(23)
l1 = [1,2,3,4,5,6,7,8,9,10]
for i in l1:
    root.insert_left(i)
root.binary_tree_print()