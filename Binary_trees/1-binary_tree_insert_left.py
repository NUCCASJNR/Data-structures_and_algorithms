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
