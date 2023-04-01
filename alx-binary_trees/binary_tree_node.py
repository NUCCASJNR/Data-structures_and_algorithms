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

    def binary_tree_print(self, prefix="", is_left=True):
        """Prints in binary tree format"""

        if self is None:
            return
        if self.right:
            self.right.binary_tree_print(prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(self.value))
        if self.left:
            self.left.binary_tree_print(prefix + ("    " if is_left else "│   "), True)

