class RootNode:
    """
    The root Node class
    """

    def __init__(self, key):
        """
        Args:
            key: node
            left: left node
            right: right node
        """
        self.value = key
        self.left = None
        self.right = None

    def search(self, data):
        if not self:
            return None

        if self.value == data:
            return self

        if data < self.value:
            return self.left.search(data) if self.left else None
        else:
            return self.right.search(data) if self.right else None

