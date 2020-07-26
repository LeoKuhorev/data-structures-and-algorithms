import pytest

from .tree import BinaryTree as bt, BinarySearchTree, Node


class TestNode:
    @pytest.fixture()
    def node(self):
        return Node(1)

    def test_proof_of_life(self):
        assert Node

    def test_repr(self, node):
        assert str(repr(node)) == 'Node(1)'

    def test_str(self, node):
        assert str(node) == 'left: (None) -- (1) -- (None) :right'

        node.left = Node(2)
        node.right = Node(3)
        assert str(node) == 'left: (2) -- (1) -- (3) :right'


class TestBinaryTree:

    def test_proof_of_life(self):
        assert bt

    @pytest.fixture()
    def tree(self):
        tree = bt('A')
        tree.root.left = Node('B')
        tree.root.right = Node('C')
        tree.root.left.left = Node('D')
        tree.root.left.right = Node('E')
        tree.root.right.left = Node('F')
        tree.root.right.right = Node('G')

        return tree

    def test_add_to_empty(self):
        tree = bt()
        tree.add(1)
        assert tree.root.val == 1

    def test_add_to_non_empty(self):
        tree = bt(1)
        tree.add(2)
        tree.add(3)
        assert tree.root.val == 1
        assert tree.root.left.val == 2
        assert tree.root.right.val == 3

    def test_pre_order_happy_path(self, tree):
        expected = ['A', 'B', 'D', 'E', 'C', 'F', 'G']
        assert tree.pre_order() == expected

    def test_in_order_happy_path(self, tree):
        expected = ['D', 'B', 'E', 'A', 'F', 'C', 'G']
        assert tree.in_order() == expected

    def test_post_order_happy_path(self, tree):
        expected = ['D', 'E', 'B', 'F', 'G', 'C', 'A']
        assert tree.post_order() == expected

    def test_contains_true(self, tree):
        assert tree.contains('A') == True

    def test_contains_false(self, tree):
        assert tree.contains('U') == False


class TestBinarySearchTree:
    def test_proof_of_life(self):
        assert BinarySearchTree

    def test_add_to_empty(self):
        bst = BinarySearchTree()
        bst.add(6)
        assert bst.root.val == 6

    def test_add_to_non_empty(self):
        bst = BinarySearchTree()
        bst.add(6)
        bst.add(4)
        bst.add(7)
        assert bst.root.val == 6
        assert bst.root.left.val == 4
        assert bst.root.right.val == 7
