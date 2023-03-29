#!/usr/bin/python3

class BinaryTreeNode:
    """The tree node class"""

    def __init__(self, parent, value):
        """
            Args:
                parent: parent node of the node to be created
                value: value to put in the new node
        """

        self.parent = parent
        self.value = value
        self.right = None
        self.left = None

    def create_node(parent, value):
        new_node = BinaryTreeNode(value, parent)
        return new_node
