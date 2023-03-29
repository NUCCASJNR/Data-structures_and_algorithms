#!/usr/bin/python3

class TreeNode:
    """Treenode class"""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.root = None

    def is_root(self, node):
        if node is None:
            return False
        if node.root is None:
            return True
        else:
            return False
