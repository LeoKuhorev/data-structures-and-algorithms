from .linked_list import LinkedList, Node
import pytest


class TestNode:
    n1 = Node(3)
    n2 = Node('test')
    n3 = Node({'key': 'value'})
    n4 = Node(False)

    def test_node1_pass(self):
        assert (self.n1.val == 3 and self.n1.next is None)

    def test_node2_pass(self):
        assert (self.n2.val == 'test' and self.n2.next is None)

    def test_node3_pass(self):
        assert (self.n3.val == {'key': 'value'} and self.n3.next is None)

    def test_node4_pass(self):
        assert (self.n4.val == False and self.n4.next is None)


class TestLinkedList:
    ll1 = LinkedList()
    ll2 = LinkedList(1)

    def test_ll_1_pass(self):
        assert self.ll1.head == None

    def test_ll_2_pass(self):
        assert isinstance(self.ll2.head, Node)

    def test_ll_3_pass(self):
        assert self.ll2.head.val == 1

    def test_ll_4_pass(self):
        assert self.ll2.head.next == None

    def test_ll_insert_1_pass(self):
        self.ll1.insert(5)
        assert self.ll1.head.val == 5

    def test_ll_insert_2_pass(self):
        assert self.ll1.head.next == None

    def test_ll_insert_3_pass(self):
        self.ll1.insert(4)
        assert self.ll1.head.val == 4

    def test_ll_insert_4_pass(self):
        assert self.ll1.head.next.val == 5

    def test_ll_insert_5_pass(self):
        self.ll1.insert(3)
        assert self.ll1.head.val == 3

    def test_ll_insert_6_pass(self):
        assert self.ll1.head.next.val == 4

    def test_ll_includes_1_pass(self):
        assert self.ll1.includes(5) == True

    def test_ll_includes_2_pass(self):
        assert self.ll1.includes(4) == True

    def test_ll_includes_3_pass(self):
        assert self.ll1.includes(3) == True

    def test_ll_includes_4_pass(self):
        assert self.ll1.includes(1) == False

    def test_ll_str_1_pass(self):
        self.ll2.insert(2)
        self.ll2.insert(3)
        self.ll2.insert(4)
        self.ll2.insert(5)
        assert str(self.ll2) == '{5} -> {4} -> {3} -> {2} -> {1} -> None'


class TestLLInsertion:
    @pytest.fixture
    def empty_ll(self):
        ll = LinkedList()
        return ll

    @pytest.fixture()
    def ll(self):
        ll = LinkedList(1)
        return ll

    def test_ll_append_edge_case(self, empty_ll):
        empty_ll.append(1)
        empty_ll.append(2)
        assert empty_ll.head.val == 1
        assert empty_ll.head.next.val == 2

    def test_ll_insert_before_1(self, empty_ll):
        """Assert it can handle an empty LL"""
        empty_ll.insert_before(1, 2)
        assert empty_ll.head is None

    def test_ll_insert_before_2(self, ll):
        """Assert it can replace the head"""
        ll.insert_before(1, 0)
        assert ll.head.val == 0
        assert ll.head.next.val == 1

    def test_ll_insert_before_3(self, ll):
        """Assert it works when the value doesn't exist in the list"""
        ll.insert_before(6, 0)
        assert ll.head.val == 1
        assert ll.head.next is None

    def test_ll_insert_after_1(self, empty_ll):
        """Assert it can handle an empty LL"""
        empty_ll.insert_after(0, 1)
        assert empty_ll.head is None

    def test_ll_insert_after_2(self, ll):
        """Assert it works when the value doesn't exist in the list"""
        ll.insert_after(6, 1)
        assert ll.head.val == 1

    def test_ll_insert_after_3(self, ll):
        """Assert it can handle an empty LL"""
        ll.insert_after(1, 2)
        assert ll.head.val == 1
        assert ll.head.next.val == 2

    def test_ll_insert_after_happy_path(self, ll):
        """Happy path"""
        ll.insert_after(1, 2)
        ll.insert_after(2, 3)
        ll.insert_after(3, 4)
        assert ll.head.val == 1
        assert ll.head.next.val == 2
        assert ll.head.next.next.val == 3
        assert ll.head.next.next.next.val == 4
