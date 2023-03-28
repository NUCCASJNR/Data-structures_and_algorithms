## Binary Trees


![Binary tree logo](https://www.tutorialspoint.com/data_structures_algorithms/images/binary_tree.jpg)
## Brief introduction to binary trees

A binary tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child. Each node in a binary tree stores some data, which can be any type of object depending on the application.

The first node of the binary tree is known as the root, and all other nodes are either a left or right child of the root or of another node in the tree. Nodes that have no children are called leaf nodes, while nodes that have one or more children are called internal nodes.

Binary trees are commonly used in computer science for a wide range of applications, including data storage and searching algorithms. They can be used to implement binary search algorithms, which can efficiently search for a particular item in a sorted list of data. Binary trees are also used in parsing and expression evaluation algorithms, and in building decision trees for machine learning algorithms.


-----------------------------------------------------------
## difference between a binary tree and a Binary Search Tree
------------------------------------------------------------

Both binary trees and binary search trees are data structures used in computer science for organizing data in a tree-like structure. However, there are some key differences between the two:

* Definition:
A binary tree is a tree data structure where each node has at most two child nodes.

A binary search tree is a binary tree where the left subtree of a node contains only nodes with keys lesser than the node’s key, and the right subtree of a node contains only nodes with keys greater than the node’s key.

* Search Operation:
In a binary tree, search operations do not take advantage of the structure of the tree. To search for a node with a given key, you must traverse the tree and check each node's key until you find a match.

In a binary search tree, the search operation takes advantage of the tree structure. You can eliminate a large portion of the tree by comparing the search key with the keys at the root and recursively traversing either the left or right subtree based on the comparison result.

* Insertion and Deletion:

In a binary tree, insertion and deletion operations are straightforward, as you simply need to add or remove nodes in the correct position in the tree. However, there is no guarantee that the resulting tree will be balanced.

In a binary search tree, insertion and deletion operations must maintain the order of the keys. If the new key is greater than the current node, it is inserted into the right subtree. If the new key is less than the current node, it is inserted into the left subtree. Deletion operations must also maintain the order of the keys, and may involve restructuring the tree to maintain balance.

In summary, a binary search tree is a specialized type of binary tree that maintains the order of its keys, allowing for efficient search operations.

-------------------------------------------------------------
## How to insert into a binary tree
-------------------------------------------------------------

* If the tree is empty, create a new node and make it the root of the tree.

* If the tree is not empty, start at the root node and compare the value of the new node to the value of the current node.

* If the new node's value is less than the current node's value, move to the left child node. If the left child node is null, create a new node and make it the left child node. If the left child node already exists, repeat step 2 with the left child node as the new current node.

* If the new node's value is greater than or equal to the current node's value, move to the right child node. If the right child node is null, create a new node and make it the right child node. If the right child node already exists, repeat step 2 with the right child node as the new current node
