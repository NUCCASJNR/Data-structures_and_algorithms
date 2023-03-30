class BinaryTreeNode:
    """The tree node class"""

    def __init__(self, parent, value):
        """
            Args:
                parent: parent node of the node to be created
                value: value to put in the new node
        """

        self.parent = parent
        self.value = value
        self.right = None
        self.left = None

    def binary_tree_print(node):
        output = _build_binary_tree_output(node)
        print(output)

    def _build_binary_tree_output(node):
        if node is None:
            return ""

        left_output = _build_binary_tree_output(node.left)
        right_output = _build_binary_tree_output(node.right)

        node_output = f"({node.value:03d})"

        if left_output and right_output:
            middle_line = f".--{left_output}--.{' ' * (9 - len(left_output) - len(right_output))}.--{right_output}--."
            output = f"{middle_line}\n{node_output}"
        elif left_output:
            middle_line = f".--{left_output}--."
            output = f"{middle_line}\n{node_output}"
        elif right_output:
            middle_line = f"{' ' * 9}.--{right_output}--."
            output = f"{node_output}\n{middle_line}"
        else:
            output = node_output

        return output

