import unittest
from main import heap_sort  

class TestHeapSort(unittest.TestCase):
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        heap_sort(arr)
        self.assertEqual(arr, expected)

    def test_reverse_array(self):
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        heap_sort(arr)
        self.assertEqual(arr, expected)

    def test_unsorted_array(self):
        arr = [12, 11, 13, 5, 6, 7]
        expected = [5, 6, 7, 11, 12, 13]
        heap_sort(arr)
        self.assertEqual(arr, expected)

    def test_with_duplicates(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        expected = sorted(arr)
        heap_sort(arr)
        self.assertEqual(arr, expected)

    def test_empty_array(self):
        arr = []
        expected = []
        heap_sort(arr)
        self.assertEqual(arr, expected)

    def test_single_element(self):
        arr = [42]
        expected = [42]
        heap_sort(arr)
        self.assertEqual(arr, expected)


if __name__ == "__main__":
    unittest.main()
