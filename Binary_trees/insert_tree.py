#!/use/bin/python3

class Bst:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, data):
        if self.key is None:
            self.key = data
        if self.key == data:
            return
        if self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Bst(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Bst(data)
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.key)
        if self.right:
            self.right.print_tree()
