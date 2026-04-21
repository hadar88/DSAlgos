import unittest
from DataStructures import DisjointSetsItem

class TestSetItem(unittest.TestCase):
    def test_create_and_destroy(self):
        item = DisjointSetsItem(10)
        self.assertIsNotNone(item)
        self.assertEqual(item.GetData(), 10)
        self.assertEqual(item.GetRank(), 0)
        # Memory is managed by the SetItem class's __del__ method

    def test_set_and_get_rank(self):
        item = DisjointSetsItem(20)
        self.assertEqual(item.GetRank(), 0)

        item.SetRank(5)
        self.assertEqual(item.GetRank(), 5)

    def test_set_and_get_parent(self):
        item1 = DisjointSetsItem(1)
        item2 = DisjointSetsItem(2)

        item2.SetParent(item1)

        parent = item2.GetParent()
        self.assertIsNotNone(parent)
        self.assertEqual(parent.GetData(), 1)

    def test_parent_chain(self):
        a = DisjointSetsItem(1)
        b = DisjointSetsItem(2)
        c = DisjointSetsItem(3)
        b.SetParent(a)
        c.SetParent(b)

        self.assertEqual(c.GetParent().GetData(), 2)
        self.assertEqual(c.GetParent().GetParent().GetData(), 1)

    def test_overwrite_rank(self):
        item = DisjointSetsItem(5)
        for rank in [0, 1, 3, 7, 10]:
            item.SetRank(rank)
            self.assertEqual(item.GetRank(), rank)

    def test_reparent(self):
        a = DisjointSetsItem(10)
        b = DisjointSetsItem(20)
        c = DisjointSetsItem(30)

        a.SetParent(b)
        self.assertEqual(a.GetParent().GetData(), 20)

        a.SetParent(c)
        self.assertEqual(a.GetParent().GetData(), 30)

if __name__ == "__main__":
    unittest.main()
