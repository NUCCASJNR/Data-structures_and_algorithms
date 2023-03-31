#!/usr/bin/python3

"""
    This module traverses a binary tree using
    pre-order traversal
"""

class PreOrder:
    """
        Defines the pre-order traversal
        class an how it works
    """
    
    def __init__(self, parent):
        """
            Initializes the class
        """
        self.parent = parent
        self.left = None
        self.right = None
        
    def pre_order_transversal(node):
        """
            This is a method that traverses a binary tree
            using pre-order traversal
            Args:
                node: root node of the binary tree
        """
        if node:
            """Checks if the node is not empty"""
            print(node.parent)
            if node.left:
                """Checks if the node has a left child"""
                node.left.pre_order_transversal()
                """Transverse the left side of the tree"""
                
            if node.right:
                """Checks if the node has a right child"""
                node.right.pre_order_transversal()
                """Transverse the right side of the tree"""