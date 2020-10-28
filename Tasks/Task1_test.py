import unittest
from Task1 import no_duplicates

class TaskTests(unittest.TestCase):
    def test_function0(self):
        self.assertEqual(no_duplicates([]), [])

    def test_function1(self):
        self.assertEqual(no_duplicates([1, 2, 3, 1]), [1, 2, 3])

    def test_function2(self):
        self.assertEqual(no_duplicates([1, 3, 2, 1, 5, 3, 6, 1, 4]), [1, 3, 2, 5, 6, 4])

    def test_function3(self):
        self.assertEqual(no_duplicates([3,3,3,3,3,3,2,1,6,6,6,4,]), [3,2,1,6,4])


if __name__ == '__main__':
    unittest.main()
