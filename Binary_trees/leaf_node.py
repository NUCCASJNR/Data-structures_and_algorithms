#!/usr/bin/python3

class TreeNode:
    """Defines the leafnode class"""

    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def leaf(self, node):
        if node is None:
            return False
        if node.left is None:
            return True
        elif node.right is None:
            return True
        else:
            return False
