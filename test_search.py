from binary_trees.search_tree import RootNode

#if __name__ == '__main__':
    # create the binary search tree
root = RootNode(8)
root.left = RootNode(3)
root.right = RootNode(10)
root.left.left = RootNode(1)
root.left.right = RootNode(6)
root.right.right = RootNode(14)
root.left.right.left = RootNode(4)
root.left.right.right = RootNode(7)
root.right.right.left = RootNode(13)

    # search for a node with value 6
searched_node = root.search(19)
if searched_node:
    print(f'Found node with value {searched_node.value}')
else:
    print('Value not found in binary search tree.')
