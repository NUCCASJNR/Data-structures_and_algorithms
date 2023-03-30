#!/usr/bin/python3

LeftNode = __import__('1-binary_tree_insert_left').LeftNode
BinaryTreeNode = __import__('0-binary_tree_node').BinaryTreeNode

if __name__ == "__main__":
    root = LeftNode(98)
    left_child = root.insert_left(2)
    right_child = root.insert_left(54)
    root.binary_tree_print()
