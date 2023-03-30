#!/usr/bin/python3

BinaryTreeNode = __import__('0-binary_tree_node').BinaryTreeNode
#from binary_tree_node import BinaryTreeNode
def main():
    root = BinaryTreeNode(87, 98)

    root.left = BinaryTreeNode(root, 12)
    root.left.left = BinaryTreeNode(root.left, 6)
    root.left.right = BinaryTreeNode(root.left, 16)

    root.right = BinaryTreeNode(root, 402)
    root.right.left = BinaryTreeNode(root.right, 256)
    root.right.right = BinaryTreeNode(root.right, 512)

    root.binary_tree_print()

if __name__  == "__main__":
    main()
