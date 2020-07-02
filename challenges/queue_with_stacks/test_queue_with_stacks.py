import pytest

from .queue_with_stacks import PseudoQueue


class TestPseudoQueue:
    @pytest.fixture()
    def queue(self):
        return PseudoQueue()

    def test_instance(self, queue):
        assert queue

    def test_enqueue(self, queue):
        assert queue.enqueue(1).val == 1
        assert queue.enqueue(2).val == 2

    def test_dequeue_error(self, queue):
        with pytest.raises(AttributeError) as err:
            assert queue.dequeue()
        assert str(err.value) == 'Cannot be called on empty queue'

    def test_dequeue(self, queue):
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.dequeue() == 4
        assert queue.dequeue() == 5
