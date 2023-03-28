#!/usr/bin/python3

from Binary_trees.leaf_node import TreeNode

#creating a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(root.leaf(root.left.left))  # Output: True
print(root.leaf(root.left.right))
