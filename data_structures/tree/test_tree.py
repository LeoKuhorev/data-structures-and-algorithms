import pytest

from .tree import BinaryTree as bt, Node


class TestBinaryTree:

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

    def test_proof_of_life(self):
        assert bt

    def test_pre_order_happy_path(self, tree):
        expected = ['A', 'B', 'D', 'E', 'C', 'F', 'G']
        assert tree.pre_order(tree.root) == expected

    def test_in_order_happy_path(self, tree):
        expected = ['D', 'B', 'E', 'A', 'F', 'C', 'G']
        assert tree.in_order(tree.root) == expected

    def test_post_order_happy_path(self, tree):
        expected = ['D', 'E', 'B', 'F', 'G', 'C', 'A']
        assert tree.post_order(tree.root) == expected
