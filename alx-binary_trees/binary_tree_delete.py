# #!/usre/bin/python3
# """This module contains a function that deletes an entire binary tree"""


# class DeleteNode:
#     """This is a class that defines a node of a Binary Tree.
#     """
#     def __init__(self, parent):
#         """This is a method that initializes a node of a Binary Tree."""
#         self.parent = parent
#         self.left = None
#         self.right = None

#     def delete_node(self):
#         """This is a method that deletes an entire binary tree."""

#         if self:
#             if self.left:
#                 self.delete_node()
#             if self.right:
#                 self.delete_node()
#         del self


class DeleteNode:
    """This is a class that defines a node of a Binary Tree.
    """
    def __init__(self, parent):
        """This is a method that initializes a node of a Binary Tree."""
        self.parent = parent
        self.left = None
        self.right = None
        self.deleted = False

    def delete_node(self):
        """This is a method that deletes an entire binary tree."""

        if self and not self.deleted:
            if self.left:
                self.left.delete_node()
            if self.right:
                self.right.delete_node()
            self.deleted = True
        del self
        print("Binary tree has been deleted!")