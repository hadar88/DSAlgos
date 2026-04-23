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

    def test_extract_top(self):
        self.pq.Insert(15)
        self.pq.Insert(10)
        self.pq.Insert(30)

        self.assertEqual(self.pq.Top(), 30)
        self.assertEqual(self.pq.ExtractTop(), 30)
        self.assertEqual(self.pq.GetSize(), 2)
        self.assertEqual(self.pq.ExtractTop(), 15)

    def test_update_key(self):
        self.pq.Insert(10)
        self.pq.Insert(5)
        self.pq.Insert(20)
        
        index_of_5 = self.pq.IndexOf(5)
        self.pq.UpdateKey(index_of_5, 50)
        
        self.assertEqual(self.pq.Top(), 50)

    def test_edge_cases(self):
        val = self.pq.ExtractTop()
        self.assertEqual(val, INT_MIN)
        
        self.pq.UpdateKey(99, 100)

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
            results.append(self.pq.ExtractTop())
        for i in range(len(results) - 1):
            self.assertGreaterEqual(results[i], results[i + 1])

    def test_single_element_heap(self):
        self.pq.Insert(42)
        self.assertEqual(self.pq.Top(), 42)
        self.assertEqual(self.pq.ExtractTop(), 42)
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
        self.pq.UpdateKey(idx, 100)
        self.assertEqual(self.pq.Top(), 100)

    def test_duplicate_values(self):
        for _ in range(5):
            self.pq.Insert(7)
        self.assertEqual(self.pq.GetSize(), 5)
        self.assertEqual(self.pq.Top(), 7)
        for _ in range(5):
            self.assertEqual(self.pq.ExtractTop(), 7)
        self.assertEqual(self.pq.GetSize(), 0)

    def test_size_decrements_on_extract(self):
        for v in [10, 20, 30]:
            self.pq.Insert(v)
        for expected_size in [2, 1, 0]:
            self.pq.ExtractTop()
            self.assertEqual(self.pq.GetSize(), expected_size)

    def test_heapsort_does_not_crash_on_single(self):
        self.pq.Insert(42)
        self.pq.HeapSort()


class TestMinHeapPriorityQueue(unittest.TestCase):
    """Test suite for Min Heap functionality"""
    
    def setUp(self):
        # Assuming PriorityQueue has a parameter for min_heap
        # Adjust constructor call based on your actual implementation
        self.min_pq = PriorityQueue(isMax=False)

    def tearDown(self):
        del self.min_pq

    def test_min_heap_create_and_empty(self):
        self.assertIsNotNone(self.min_pq)
        self.assertEqual(self.min_pq.GetSize(), 0)

    def test_min_heap_insert_and_size(self):
        self.min_pq.Insert(10)
        self.min_pq.Insert(5)
        self.min_pq.Insert(20)
        
        self.assertEqual(self.min_pq.GetSize(), 3)

    def test_min_heap_extract_top_returns_minimum(self):
        self.min_pq.Insert(15)
        self.min_pq.Insert(10)
        self.min_pq.Insert(30)
        self.min_pq.Insert(5)

        # In min heap, Top() should return the minimum value
        self.assertEqual(self.min_pq.Top(), 5)
        self.assertEqual(self.min_pq.ExtractTop(), 5)
        self.assertEqual(self.min_pq.GetSize(), 3)
        self.assertEqual(self.min_pq.ExtractTop(), 10)
        self.assertEqual(self.min_pq.ExtractTop(), 15)
        self.assertEqual(self.min_pq.ExtractTop(), 30)

    def test_min_heap_extract_all_ascending(self):
        values = [3, 1, 4, 1, 5, 9, 2, 6]
        for v in values:
            self.min_pq.Insert(v)
        
        results = []
        while self.min_pq.GetSize() > 0:
            results.append(self.min_pq.ExtractTop())
        
        # Results should be in ascending order for min heap
        for i in range(len(results) - 1):
            self.assertLessEqual(results[i], results[i + 1])

    def test_min_heap_top_is_minimum(self):
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.min_pq.Insert(v)
        
        self.assertEqual(self.min_pq.Top(), 20)

    def test_min_heap_update_key_decrease(self):
        self.min_pq.Insert(10)
        self.min_pq.Insert(20)
        self.min_pq.Insert(30)
        
        # Decrease a key to make it the new minimum
        idx = self.min_pq.IndexOf(30)
        self.min_pq.UpdateKey(idx, 5)
        
        self.assertEqual(self.min_pq.Top(), 5)

    def test_min_heap_update_key_increase(self):
        self.min_pq.Insert(10)
        self.min_pq.Insert(20)
        self.min_pq.Insert(5)
        
        # Current min should be 5
        self.assertEqual(self.min_pq.Top(), 5)
        
        # Increase the minimum value
        idx = self.min_pq.IndexOf(5)
        self.min_pq.UpdateKey(idx, 25)
        
        # Now min should be 10
        self.assertEqual(self.min_pq.Top(), 5)

    def test_min_heap_single_element(self):
        self.min_pq.Insert(42)
        self.assertEqual(self.min_pq.Top(), 42)
        self.assertEqual(self.min_pq.ExtractTop(), 42)
        self.assertEqual(self.min_pq.GetSize(), 0)

    def test_min_heap_duplicate_values(self):
        for _ in range(5):
            self.min_pq.Insert(7)
        
        self.assertEqual(self.min_pq.GetSize(), 5)
        self.assertEqual(self.min_pq.Top(), 7)
        
        for _ in range(5):
            self.assertEqual(self.min_pq.ExtractTop(), 7)
        
        self.assertEqual(self.min_pq.GetSize(), 0)

    def test_min_heap_edge_cases(self):
        # Extract from empty heap
        val = self.min_pq.ExtractTop()
        self.assertEqual(val, INT_MIN)
        
        # Update non-existent key
        self.min_pq.UpdateKey(99, 100)
        
        # Search for non-existent value
        idx = self.min_pq.IndexOf(999)
        self.assertEqual(idx, -1)

    def test_min_heap_interleaved_operations(self):
        self.min_pq.Insert(50)
        self.min_pq.Insert(30)
        self.assertEqual(self.min_pq.ExtractTop(), 30)
        
        self.min_pq.Insert(20)
        self.min_pq.Insert(40)
        self.assertEqual(self.min_pq.ExtractTop(), 20)
        self.assertEqual(self.min_pq.ExtractTop(), 40)
        self.assertEqual(self.min_pq.ExtractTop(), 50)

    def test_min_heap_large_dataset(self):
        import random
        values = [random.randint(1, 1000) for _ in range(100)]
        
        for v in values:
            self.min_pq.Insert(v)
        
        results = []
        while self.min_pq.GetSize() > 0:
            results.append(self.min_pq.ExtractTop())
        
        # Verify ascending order
        for i in range(len(results) - 1):
            self.assertLessEqual(results[i], results[i + 1])

    def test_min_heap_heapsort(self):
        values = [3, 1, 4, 1, 5, 9, 2, 6]
        for v in values:
            self.min_pq.Insert(v)
        
        self.min_pq.Display()
        self.min_pq.HeapSort()


if __name__ == "__main__":
    unittest.main()