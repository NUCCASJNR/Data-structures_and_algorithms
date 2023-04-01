#!/usr/bin/python3

DeleteNode = __import__('binary_tree_delete').DeleteNode

root = DeleteNode(1)
root.left = DeleteNode(2)
root.right = DeleteNode(3)
root.left.right = DeleteNode(4)
root.right.left = DeleteNode(5)
root.delete_node()