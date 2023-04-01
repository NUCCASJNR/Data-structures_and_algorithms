
from binary_tree_is_root import Root
from binary_tree_node import BinaryTreeNode
from binary_tree_insert_right import RightNode
from binary_tree_insert_left import LeftNode
from binary_tree_is_root import Root

root = BinaryTreeNode(None, 98)
root.left = BinaryTreeNode(None, 12)
root.right = BinaryTreeNode(None, 402)
root.left.left = BinaryTreeNode(None, 6)
root.left.right
root.binary_tree_print()
print()
ret = Root.is_root(root)
print("Is root: {}".format(ret))
rt = Root.is_root(root.left)
print("Is root: {}".format(rt))
r1 = Root.is_root(root.left.left)
print("Is root: {}".format(r1))