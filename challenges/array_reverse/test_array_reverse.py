import unittest
from .array_reverse import reverse_array as ra


class TestUnits(unittest.TestCase):
    def test_array_reverse(self):
        self.assertEqual(ra([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(ra([]), [])
        self.assertEqual(ra([-5, -4, -3, -2, -1, 0]), [0, -1, -2, -3, -4, -5])
