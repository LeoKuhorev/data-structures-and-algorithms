class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self.val

    def __str__(self):
        return self.val


class BinaryTree:
    def __init__(self, val):
        self.root = Node(val)

    def pre_order(self, node=None, output=None):
        # root >> left >> right
        if node is None:
            node = self.root

        if output is None:
            output = []

        output.append(node.val)

        if node.left:
            output = self.pre_order(node.left, output)
        if node.right:
            output = self.pre_order(node.right, output)

        return output

    def in_order(self, node=None, output=None):
        # left >> root >> right
        if node is None:
            node = self.root

        if output is None:
            output = []

        if node.left:
            output = self.in_order(node.left, output)

        output.append(node.val)

        if node.right:
            output = self.in_order(node.right, output)

        return output

    def post_order(self, node=None, output=None):
        # left >> right >> root
        if node is None:
            node = self.root

        if output is None:
            output = []

        if node.left:
            output = self.post_order(node.left, output)

        if node.right:
            output = self.post_order(node.right, output)

        output.append(node.val)

        return output
