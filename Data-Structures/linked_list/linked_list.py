class Node:
    """Class Node"""

    def __init__(self, val: any) -> None:
        """class Constructor

        Args:
            val (any): Value to be saved within the node
        """
        self.val = val
        self.next = None


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
        while not curr is None:
            if curr.val == target:
                return True
            curr = curr.next
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
