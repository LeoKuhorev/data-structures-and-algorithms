from data_structures.stacks_and_queues.stacks_and_queues import Queue


class Node:
    """Node class
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.__class__.__name__}({self.val})'

    def __str__(self):
        l = self.left.val if self.left else None
        r = self.right.val if self.right else None
        return f'left: ({l}) -- ({self.val}) -- ({r}) :right'


class BinaryTree:
    """Binary Tree class
    """

    def __init__(self, val=None):
        self.root = Node(val) if val else None

    def add(self, val: any) -> None:
        """Add a new node with Breadth first approach

        Args:
            val (any): Value to add
        """
        new_node = Node(val)
        if self.root:
            q = Queue()
            q.enqueue(self.root)

            def node_exists(node):
                if node:
                    q.enqueue(node)
                    return True
                return False

            while not q.is_empty():
                node = q.dequeue()

                if node_exists(node.left):
                    if not node_exists(node.right):
                        node.right = new_node
                else:
                    node.left = new_node

        else:
            self.root = new_node

    def contains(self, val):
        def traverse(node):
            if node:
                if node.val == val:
                    return True
                traverse(node.left)
                traverse(node.right)
                return False

        return traverse(self.root)

    def pre_order(self):
        # root >> left >> right
        output = []

        def traverse(node):
            if node:
                output.append(node.val)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)

        return output

    def in_order(self):
        # left >> root >> right
        output = []

        def traverse(node):
            if node:
                traverse(node.left)
                output.append(node.val)
                traverse(node.right)

        traverse(self.root)

        return output

    def post_order(self):
        # left >> right >> root
        output = []

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                output.append(node.val)

        traverse(self.root)

        return output


class BinarySearchTree(BinaryTree):
    def add(self, val):
        new_node = Node(val)

        def traverse(node):
            if new_node.val < node.val:
                if node.left:
                    traverse(node.left)
                else:
                    node.left = new_node
            else:
                if node.right:
                    traverse(node.right)
                else:
                    node.right = new_node

        if self.root:
            traverse(self.root)
        else:
            self.root = new_node


bt = BinaryTree()
bt.add(1)
bt.add(2)

print(bt.pre_order())
