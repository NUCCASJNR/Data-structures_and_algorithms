#!/usr/bin/python3

"""
This module checks if a node is a root
"""

class Root:
    """
    Defines the class
    """
    
    def __init__(self, parent):
        """
        Initializes the class
        Args:
            parent: a reference to a node in a binary tree
        """
        self.parent = parent
        self.left = None
        self.right = None
        
    def is_root(self):
        """This method checks if a node is a root
        Return:
            1 if the node is a root
            0 if the node is not a root
        """
        if self.parent is None:
            """Node has no parent"""
            return 1
        elif self.left is not None:
            """ left Node has at least one child
            so it is not a root node
            """
            return 0
        elif self.right is not None:
            """ right Node has at least one child
            so it is not a root node
            """
            return 0
        else:
            """Node has a parent and no children"""
            return 1
        
   