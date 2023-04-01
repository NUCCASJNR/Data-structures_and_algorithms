#!/usr/bin/python3

LeafNode = __import__('binary_tree_is_leaf').LeafNode
root = LeafNode(8)
root.left = LeafNode(3)
root.right = LeafNode(10)
root.left.left = LeafNode(1)
root.left.right = LeafNode(6)
root.right.left = LeafNode(9)
root.right.right = LeafNode(14)

"""Creating a list that will hold all the nodes i wanna check for"""
nodes_to_check = [root, root.left, root.right, root.left.left, root.left.right, root.right.left, root.right.right]
for i in nodes_to_check:
    if i.is_leaf():
        print(f"Node {i.parent} is a leaf node")
    else:
        print(f"Node {i.parent} is not a leaf node")