#!/usr/bin/python3

RightNode = __import__('2-binary_tree_insert_right').RightNode

root = RightNode(23)
l1 = [1,2,3,4,5,6,7,8,9,10]
for i in l1:
    root.right_node(i)
root.binary_tree_print()