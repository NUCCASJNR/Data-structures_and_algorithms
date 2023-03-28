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
        self.key = key
        self.left = None
        self.right = None

    def search(self, data):
        if not self:
            return None

        if self.key == data:
            return self

        if data < self.key:
            if self.left:
                return self.left.search(data)
            else:
                return None
        elif  data > self.key:
            if self.right:
                return self.right.search(data)
            else:
                return None
