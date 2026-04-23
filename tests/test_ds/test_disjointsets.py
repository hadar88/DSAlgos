import unittest
from DataStructures import DisjointSets

class TestDisjointSets(unittest.TestCase):
    def setUp(self):
        self.ds = DisjointSets()

    def tearDown(self):
        del self.ds

    def test_create_and_empty(self):
        self.assertIsNotNone(self.ds)

    def test_makeset_and_findset(self):
        self.ds.MakeSet(10)
        self.ds.MakeSet(20)

        item10 = self.ds.FindSet(10)
        self.assertIsNotNone(item10)
        self.assertEqual(item10.GetData(), 10)

        self.assertIsNone(self.ds.FindSet(30))

    def test_union(self):
        self.ds.MakeSet(1)
        self.ds.MakeSet(2)
        self.ds.MakeSet(3)

        self.ds.Union(1, 2)

        root1 = self.ds.FindSet(1)
        root2 = self.ds.FindSet(2)
        self.assertIsNotNone(root1)
        self.assertEqual(root1.GetData(), root2.GetData())

        self.ds.Union(2, 3)
        root3 = self.ds.FindSet(3)
        self.assertEqual(root1.GetData(), root3.GetData())

    def test_edge_cases(self):
        self.ds.Union(100, 200)
        self.assertIsNone(self.ds.FindSet(999))

    def test_display(self):
        self.ds.MakeSet(1)
        self.ds.Display()

    def test_union_transitivity(self):
        for v in [1, 2, 3]:
            self.ds.MakeSet(v)
        self.ds.Union(1, 2)
        self.ds.Union(2, 3)
        r1 = self.ds.FindSet(1).GetData()
        r2 = self.ds.FindSet(2).GetData()
        r3 = self.ds.FindSet(3).GetData()
        self.assertEqual(r1, r2)
        self.assertEqual(r2, r3)

    def test_independent_sets(self):
        self.ds.MakeSet(10)
        self.ds.MakeSet(20)
        r10 = self.ds.FindSet(10).GetData()
        r20 = self.ds.FindSet(20).GetData()
        self.assertNotEqual(r10, r20)

    def test_self_union(self):
        self.ds.MakeSet(5)
        self.ds.Union(5, 5)
        root = self.ds.FindSet(5)
        self.assertIsNotNone(root)
        self.assertEqual(root.GetData(), 5)

    def test_large_union_all_same_set(self):
        values = list(range(1, 11))
        for v in values:
            self.ds.MakeSet(v)
        for i in range(len(values) - 1):
            self.ds.Union(values[i], values[i + 1])
        root_val = self.ds.FindSet(values[0]).GetData()
        for v in values:
            self.assertEqual(self.ds.FindSet(v).GetData(), root_val)

    def test_two_independent_components(self):
        for v in range(1, 7):
            self.ds.MakeSet(v)
        self.ds.Union(1, 2)
        self.ds.Union(2, 3)
        self.ds.Union(4, 5)
        self.ds.Union(5, 6)
        root_a = self.ds.FindSet(1).GetData()
        root_b = self.ds.FindSet(4).GetData()
        self.assertNotEqual(root_a, root_b)
        for v in [1, 2, 3]:
            self.assertEqual(self.ds.FindSet(v).GetData(), root_a)
        for v in [4, 5, 6]:
            self.assertEqual(self.ds.FindSet(v).GetData(), root_b)

    def test_display_multiple_sets(self):
        for v in [10, 20, 30]:
            self.ds.MakeSet(v)
        self.ds.Union(10, 20)
        self.ds.Display()

if __name__ == "__main__":
    unittest.main()
