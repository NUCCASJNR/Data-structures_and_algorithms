
from binary_tree_is_root import Root
from binary_tree_node import BinaryTreeNode
from binary_tree_insert_right import RightNode
from binary_tree_insert_left import LeftNode
from binary_tree_is_root import Root

root = BinaryTreeNode(None, 98)
root.left = BinaryTreeNode(None, 12)
root.right = BinaryTreeNode(None, 128)
root.left.right = BinaryTreeNode(None, 54)
root.right.right = BinaryTreeNode(None, 402)
root.binary_tree_print()
print()

# root_obj = Root(root)
ret = Root.is_root(root)
print(f"Is {root.value} a root: {ret}")
rt = Root.is_root(root.right)
print(f"Is {root.right.value} a root: {rt}")
r1 = Root.is_root(root.right.right)
print(f"Is {root.right.right.value} a root: {r1}")