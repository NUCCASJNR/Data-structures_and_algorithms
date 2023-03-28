#!/usr/bin/python3
from Binary_trees.binary_tree_print import Test
from Binary_trees.insert_tree import Bst

bst = Bst(9)

# insert some values into the BST
bst.insert(10)
bst.insert(15)
bst.insert(7)
bst.insert(12)
bst.insert(20)
bst.insert(89)
bst.print_tree()
print()

list1 = [90, 45, 78, 2, 6, 7, 7, 10]
for i in list1:
    bst.insert(i)
bst.print_tree()
