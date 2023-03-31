#!/usr/bin/python3

"""This module checks if a node is a leaf"""


class LeafNode:
    """creates the leafnode class"""
    
    def __init__(self, parent):
        """initializes the class"""
        self.parent = parent
        self.left = None
        self.right = None
        
    def is_leaf(node):
        """checks if the node of a binary tree is a 
            leaf Node
        """
        if node is None:
            return False
        if node.right is None:
            return True
        if node.right is None:
            return True
        return False