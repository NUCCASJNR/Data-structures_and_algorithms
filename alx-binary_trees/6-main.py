#!/usr/bin/python3
"""
    importing the BinaryTreeNode class that creates
    a Binary tree node
"""

BinaryTreeNode = __import__('0-binary_tree_node').BinaryTreeNode
root = BinaryTreeNode(None, 98)

root.left = BinaryTreeNode(root, 12)
root.left.left = BinaryTreeNode(root.left, 6)
root.left.right = BinaryTreeNode(root.left, 16)

root.right = BinaryTreeNode(root, 402)
root.right.left = BinaryTreeNode(root.right, 256)
root.right.right = BinaryTreeNode(root.right, 512)

root.binary_tree_print()

print("Transversal in pre-order below:")

"""
    importing the PreOrder class that transverses a binary tree
    in the pre-order transversal method to print the nodes
    in the binary tree created by the BinaryTreeNode class in pre
    order transversal method
"""
PreOrder = __import__('6-binary_tree_preorder').PreOrder

root = PreOrder(98)
root.left = PreOrder(12)
root.right = PreOrder(402)
root.left.left = PreOrder(6)
root.left.right = PreOrder(56)
root.right.left = PreOrder(256)
root.right.right = PreOrder(512)

PreOrder.pre_order_transversal(root)