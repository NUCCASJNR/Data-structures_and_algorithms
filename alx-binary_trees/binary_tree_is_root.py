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
            return 1
        elif self.parent is not None:
            return 0
        