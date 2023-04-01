#!/usr/bin/python3

"""This module inserts a node as the left-child of another node"""

class  LeftNode:
    """The class"""

    def __init__(self, parent):
        """
        Args:
            parent:  a reference to a node in a binary tree
        """

        self.parent = parent
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.parent is None:
            self.parent = value
        if self.left:
            self.left.insert_left(value)
        else:
            self.left = LeftNode(value)
    def binary_tree_print(self, prefix="", is_left=True):
        """Prints in binary tree format"""

        if self is None:
            return
        if self.right:
            self.right.binary_tree_print(prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(self.parent))
        if self.left:
            self.left.binary_tree_print(prefix + ("    " if is_left else "│   "), True) 
