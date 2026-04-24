import unittest
from DataStructures import SkipList

class TestSkipList(unittest.TestCase):
    def setUp(self):
        self.sl = SkipList()

    def tearDown(self):
        del self.sl

    def test_create_and_empty(self):
        self.assertIsNotNone(self.sl)
        self.assertTrue(self.sl.IsEmpty())
        
        head = self.sl.GetHead()
        self.assertIsNone(head)

    def test_insert_and_search(self):
        self.sl.Insert(10)
        self.sl.Insert(20)
        self.sl.Insert(30)

        self.assertFalse(self.sl.IsEmpty())

        node20 = self.sl.Search(20)
        self.assertIsNotNone(node20)
        self.assertEqual(node20.GetData(), 20)

        node99 = self.sl.Search(99)
        self.assertIsNone(node99)

    def test_delete(self):
        self.sl.Insert(50)
        self.sl.Insert(60)

        self.sl.Delete(50)
        self.assertIsNone(self.sl.Search(50))

        self.sl.Delete(100)

    def test_display(self):
        self.sl.Insert(5)
        self.sl.Display()

    def test_edge_cases(self):
        self.assertIsNone(self.sl.Search(10))
        self.sl.Delete(10)
        self.assertIsNotNone(self.sl.GetHeight())

    def test_insert_many_and_search(self):
        values = [3, 7, 1, 9, 4, 6, 2, 8, 5]
        for v in values:
            self.sl.Insert(v)
        self.assertFalse(self.sl.IsEmpty())
        for v in values:
            node = self.sl.Search(v)
            self.assertIsNotNone(node, f"Expected to find {v}")
        self.assertIsNone(self.sl.Search(100))

    def test_delete_then_reinsert(self):
        self.sl.Insert(42)
        self.sl.Delete(42)
        self.assertIsNone(self.sl.Search(42))
        self.sl.Insert(42)
        self.assertIsNotNone(self.sl.Search(42))

    def test_duplicate_insert(self):
        self.sl.Insert(10)
        self.sl.Insert(10)
        self.assertIsNotNone(self.sl.Search(10))

    def test_delete_all_elements(self):
        values = [5, 10, 15, 20]
        for v in values:
            self.sl.Insert(v)
        for v in values:
            self.sl.Delete(v)
        self.assertTrue(self.sl.IsEmpty())
        for v in values:
            self.assertIsNone(self.sl.Search(v))

    def test_search_after_each_insert(self):
        for v in [100, 50, 150, 25, 75]:
            self.sl.Insert(v)
            node = self.sl.Search(v)
            self.assertIsNotNone(node, f"{v} not found right after insert")

    def test_display_multiple_elements(self):
        for v in [3, 1, 4, 1, 5, 9, 2, 6]:
            self.sl.Insert(v)
        self.sl.Display()

    def test_negative_values(self):
        for v in [-30, -10, -20]:
            self.sl.Insert(v)
        self.assertIsNotNone(self.sl.Search(-10))
        self.assertIsNone(self.sl.Search(-99))
        self.sl.Delete(-10)
        self.assertIsNone(self.sl.Search(-10))

if __name__ == "__main__":
    unittest.main()
