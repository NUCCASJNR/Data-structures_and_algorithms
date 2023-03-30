#!/usr/bin/python3

"""This is a function that inserts a node as the right-child of another node."""
class RightNode:
    """This is a class that defines a node of a Binary Tree."""

    def __init__(self, data, parent=None, left=None, right=None):
        """This is a method that initializes a node of a Binary Tree."""
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def right_node(self, value):
        """This is a method that inserts a node as the right-child of another node."""
        if self.parent is None:
            self.parent = value
        if self.right:
            self.right.right_node(value)
        else:
            self.right = RightNode(value)
            
    
    def binary_tree_print(self, prefix="", is_left=True):
        """Prints in binary tree format"""

        if self is None:
            return
        if self.right:
            self.right.binary_tree_print(prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(self.parent))
        if self.left:
            self.left.binary_tree_print(prefix + ("    " if is_left else "│   "), True) 