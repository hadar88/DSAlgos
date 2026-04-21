import unittest
from DataStructures import PriorityQueue
from DataStructures_py.Utils import INT_MIN

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()

    def tearDown(self):
        # Memory is managed by the PriorityQueue class's __del__ method
        del self.pq

    def test_create_and_empty(self):
        self.assertIsNotNone(self.pq)
        self.assertEqual(self.pq.GetSize(), 0)

    def test_insert_and_size(self):
        self.pq.Insert(10)
        self.pq.Insert(5)
        self.pq.Insert(20)
        
        self.assertEqual(self.pq.GetSize(), 3)

    def test_extract_max(self):
        self.pq.Insert(15)
        self.pq.Insert(10)
        self.pq.Insert(30)

        self.assertEqual(self.pq.Maximum(), 30)
        self.assertEqual(self.pq.ExtractMax(), 30)
        self.assertEqual(self.pq.GetSize(), 2)
        self.assertEqual(self.pq.ExtractMax(), 15)

    def test_increase_key(self):
        self.pq.Insert(10)
        self.pq.Insert(5)
        self.pq.Insert(20)
        
        index_of_5 = self.pq.IndexOf(5)
        self.pq.IncreaseKey(index_of_5, 50)
        
        self.assertEqual(self.pq.Maximum(), 50)

    def test_edge_cases(self):
        val = self.pq.ExtractMax()
        self.assertEqual(val, INT_MIN)
        
        self.pq.IncreaseKey(99, 100)

        idx = self.pq.IndexOf(999)
        self.assertEqual(idx, -1)

    def test_heapsort_and_display(self):
        self.pq.Insert(1)
        self.pq.Insert(2)
        self.pq.Display()
        self.pq.HeapSort()

    def test_extract_all_descending(self):
        values = [3, 1, 4, 1, 5, 9, 2, 6]
        for v in values:
            self.pq.Insert(v)
        results = []
        while self.pq.GetSize() > 0:
            results.append(self.pq.ExtractMax())
        for i in range(len(results) - 1):
            self.assertGreaterEqual(results[i], results[i + 1])

    def test_single_element_heap(self):
        self.pq.Insert(42)
        self.assertEqual(self.pq.Maximum(), 42)
        self.assertEqual(self.pq.ExtractMax(), 42)
        self.assertEqual(self.pq.GetSize(), 0)

    def test_index_of_existing(self):
        self.pq.Insert(100)
        self.pq.Insert(50)
        idx = self.pq.IndexOf(100)
        self.assertGreaterEqual(idx, 0)

    def test_increase_to_new_max(self):
        self.pq.Insert(5)
        self.pq.Insert(10)
        idx = self.pq.IndexOf(5)
        self.pq.IncreaseKey(idx, 100)
        self.assertEqual(self.pq.Maximum(), 100)

    def test_duplicate_values(self):
        for _ in range(5):
            self.pq.Insert(7)
        self.assertEqual(self.pq.GetSize(), 5)
        self.assertEqual(self.pq.Maximum(), 7)
        for _ in range(5):
            self.assertEqual(self.pq.ExtractMax(), 7)
        self.assertEqual(self.pq.GetSize(), 0)

    def test_size_decrements_on_extract(self):
        for v in [10, 20, 30]:
            self.pq.Insert(v)
        for expected_size in [2, 1, 0]:
            self.pq.ExtractMax()
            self.assertEqual(self.pq.GetSize(), expected_size)

    def test_heapsort_does_not_crash_on_single(self):
        self.pq.Insert(42)
        self.pq.HeapSort()

if __name__ == "__main__":
    unittest.main()
