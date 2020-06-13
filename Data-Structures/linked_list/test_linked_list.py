from .linked_list import LinkedList, Node


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
