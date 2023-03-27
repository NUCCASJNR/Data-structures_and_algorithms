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


# create a new BST with a root node value of 10
bst = Bst(10)

# insert some values into the BST
bst.insert(10)
bst.insert(15)
bst.insert(7)
bst.insert(12)
bst.insert(20)
bst.insert(89)
list1 = [90, 67, 32, 1, 4, 6]
for i in list1:
    bst.insert(i)
# print the values of all nodes in ascending order
bst.print_tree()
