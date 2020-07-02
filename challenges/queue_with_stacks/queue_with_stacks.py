from data_structures.stacks_and_queues.stacks_and_queues import Stack


class PseudoQueue:
    def __init__(self):
        self.add = Stack()
        self.remove = Stack()

    def enqueue(self, val):
        try:
            while self.remove.peek():
                self.add.push(self.remove.pop())
        except AttributeError as err:
            pass

        self.add.push(val)
        return self.add.top

    def dequeue(self):
        try:
            while self.add.peek():
                self.remove.push(self.add.pop())
        except AttributeError as err:
            pass

        try:
            return self.remove.pop()
        except AttributeError as err:
            raise AttributeError('Cannot be called on empty queue')
