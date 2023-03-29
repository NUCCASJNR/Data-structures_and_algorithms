#!/usr/bin/python3

from Binary_trees.root_node import TreeNode

root = TreeNode(1)
root.left = TreeNode(2)
root.left.root = root.left
print(root.is_root(root))
print(root.is_root(root.left))
