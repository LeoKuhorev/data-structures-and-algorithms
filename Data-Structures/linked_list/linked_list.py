class Node:
    """Class Node"""

    def __init__(self, val: any) -> None:
        """class Constructor

        Args:
            val (any): Value to be saved within the node
        """
        self.val = val
        self.next = None

    def __str__(self):
        return f'{{{self.val}}}'

    def __repr__(self):
        return f'Node({self.val})'


class LinkedList:
    """Class Singly Linked List"""

    def __init__(self, val=None) -> None:
        """class Constructor

        Args:
            val (any, optional): Value to be passed to the head node upon LL instantiation. Defaults to None.
        """
        self.head = None
        if not val is None:
            new_node = Node(val)
            self.head = new_node

    def insert(self, val: any) -> None:
        """Prepends a new instance of Node class with a given value before LL head node

        Args:
            val (any): Value to be passed over to the Node
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def includes(self, target: any) -> bool:
        """Traverses the LL and returns whether the given value is present in the List

        Args:
            target (any): Value to look for

        Returns:
            bool: Whether the value was found
        """
        curr = self.head
        while curr:
            if curr.val == target:
                return True
            curr = curr.next
        return False

    def append(self, val: any) -> None:
        """Appends a node with the given value to the end of the Linked List

        Args:
            val (any): Value to be passed in
        """
        new_node = Node(val)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        else:
            self.head = new_node

    def insert_before(self, val: any, new_val: any) -> bool:
        """Inserts a node with the given new value before the first occurence of the given target value. Returns False otherwise

        Args:
            val (any): Target value to look for
            new_val (any): New value to be passed in

        Returns:
            bool: Whether the insertion was successful
        """
        curr = prev = self.head
        while curr:
            if curr.val == val:
                new_node = Node(new_val)
                if curr == self.head:
                    self.head = new_node
                    new_node.next = curr
                else:
                    prev.next = new_node
                    new_node.next = curr
                return True
            else:
                prev, curr = curr, curr.next
        else:
            return False

    def insert_after(self, val: any, new_val: any) -> bool:
        """Inserts a node with the given new value after the first occurence of the given target value. Returns False otherwise

        Args:
            val (any): Target value to look for
            new_val (any): New value to be passed in

        Returns:
            bool: Whether the insertion was successful
        """
        curr = self.head
        while curr:
            if curr.val == val:
                new_node = Node(new_val)
                new_node.next = curr.next
                curr.next = new_node
                return True
            else:
                curr = curr.next
        else:
            return False

    def __str__(self) -> str:
        """LL class String representation

        Returns:
            str: Visual LL representation
        """
        curr = self.head
        output = ''
        while not curr is None:
            output += f'{{{ curr.val }}} -> '
            curr = curr.next
        output += 'None'
        return output
