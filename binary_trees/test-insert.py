#!/usr/bin/python3
Bst = __import__('insert_tree').Bst

bst = Bst(9)

# insert some values into the BST
bst.insert(10)
bst.insert(15)
bst.insert(7)
bst.insert(12)
bst.insert(20)
bst.insert(89)
bst.print_tree()
