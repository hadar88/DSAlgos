import unittest
from Algos import Sorts

class TestSorts(unittest.TestCase):
    def setUp(self):
        self.unsorted = [64, 34, 25, 12, 22, 11, 90]
        self.sorted = [11, 12, 22, 25, 34, 64, 90]
        self.reverse = [90, 64, 34, 25, 22, 12, 11]
        self.duplicates = [5, 1, 9, 5, 2, 1, 5]
        self.sorted_duplicates = [1, 1, 2, 5, 5, 5, 9]

    def test_insertion_sort(self):
        self.assertEqual(Sorts.InsertionSort(self.unsorted), self.sorted)
        self.assertEqual(Sorts.InsertionSort(self.sorted), self.sorted)
        self.assertEqual(Sorts.InsertionSort(self.reverse), self.sorted)
        self.assertEqual(Sorts.InsertionSort(self.duplicates), self.sorted_duplicates)
        self.assertEqual(Sorts.InsertionSort([]), [])
        self.assertEqual(Sorts.InsertionSort([1]), [1])

    def test_merge_sort(self):
        self.assertEqual(Sorts.MergeSort(self.unsorted), self.sorted)
        self.assertEqual(Sorts.MergeSort(self.sorted), self.sorted)
        self.assertEqual(Sorts.MergeSort(self.reverse), self.sorted)
        self.assertEqual(Sorts.MergeSort(self.duplicates), self.sorted_duplicates)
        self.assertEqual(Sorts.MergeSort([]), [])
        self.assertEqual(Sorts.MergeSort([1]), [1])

    def test_quick_sort(self):
        self.assertEqual(Sorts.QuickSort(self.unsorted), self.sorted)
        self.assertEqual(Sorts.QuickSort(self.sorted), self.sorted)
        self.assertEqual(Sorts.QuickSort(self.reverse), self.sorted)
        self.assertEqual(Sorts.QuickSort(self.duplicates), self.sorted_duplicates)
        self.assertEqual(Sorts.QuickSort([]), [])
        self.assertEqual(Sorts.QuickSort([1]), [1])

    def test_counting_sort(self):
        self.assertEqual(Sorts.CountingSort(self.unsorted), self.sorted)
        self.assertEqual(Sorts.CountingSort(self.sorted), self.sorted)
        self.assertEqual(Sorts.CountingSort(self.reverse), self.sorted)
        self.assertEqual(Sorts.CountingSort(self.duplicates), self.sorted_duplicates)
        self.assertEqual(Sorts.CountingSort([]), [])
        self.assertEqual(Sorts.CountingSort([1]), [1])
        
        self.assertIsNone(Sorts.CountingSort([-1, 2, 3]))

    def test_identical_elements(self):
        identical = [5, 5, 5, 5, 5]
        self.assertEqual(Sorts.InsertionSort(identical), identical)
        self.assertEqual(Sorts.MergeSort(identical), identical)
        self.assertEqual(Sorts.QuickSort(identical), identical)
        self.assertEqual(Sorts.CountingSort(identical), identical)

    def test_alternating_elements(self):
        alternating = [1, 2, 1, 2, 1, 2]
        expected = [1, 1, 1, 2, 2, 2]
        self.assertEqual(Sorts.InsertionSort(alternating), expected)
        self.assertEqual(Sorts.MergeSort(alternating), expected)
        self.assertEqual(Sorts.QuickSort(alternating), expected)
        self.assertEqual(Sorts.CountingSort(alternating), expected)

    def test_counting_sort_large_range(self):
        large_range = [1000, 0, 500, 1, 999]
        expected = [0, 1, 500, 999, 1000]
        self.assertEqual(Sorts.CountingSort(large_range), expected)

    def test_large_array(self):
        large_array = list(range(100, 0, -1))
        expected = list(range(1, 101))
        
        self.assertEqual(Sorts.InsertionSort(large_array), expected)
        self.assertEqual(Sorts.MergeSort(large_array), expected)
        self.assertEqual(Sorts.QuickSort(large_array), expected)
        self.assertEqual(Sorts.CountingSort(large_array), expected)

if __name__ == "__main__":
    unittest.main()
