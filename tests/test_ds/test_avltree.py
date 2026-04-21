import unittest
from DataStructures import AVLTree
from DataStructures_py.Utils import INT_MAX, INT_MIN

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()

    def tearDown(self):
        # Memory is managed by the AVLTree class's __del__ method
        del self.tree

    def test_create_and_empty(self):
        self.assertIsNotNone(self.tree)
        self.assertTrue(self.tree.IsEmpty())
        self.assertEqual(self.tree.Size(), 0)

    def test_insert_and_balance(self):
        self.tree.Insert(10)
        self.tree.Insert(20)
        self.tree.Insert(30)

        root = self.tree.GetRoot()
        self.assertIsNotNone(root)
        self.assertEqual(root.GetData(), 20)
        
        self.assertEqual(self.tree.Size(), 3)

    def test_search_and_exists(self):
        self.tree.Insert(50)
        self.tree.Insert(40)
        
        self.assertTrue(self.tree.Exists(40))
        self.assertFalse(self.tree.Exists(100))

        node = self.tree.Search(50)
        self.assertIsNotNone(node)
        self.assertEqual(node.GetData(), 50)

    def test_delete(self):
        self.tree.Insert(50)
        self.tree.Insert(30)
        self.tree.Insert(70)

        self.tree.Delete(30)
        self.assertFalse(self.tree.Exists(30))
        self.assertEqual(self.tree.Size(), 2)

    def test_min_max(self):
        self.tree.Insert(15)
        self.tree.Insert(10)
        self.tree.Insert(20)

        self.assertEqual(self.tree.Minimum(), 10)
        self.assertEqual(self.tree.Maximum(), 20)

    def test_successor(self):
        self.tree.Insert(10)
        self.tree.Insert(20)
        
        succ = self.tree.Successor(10)
        self.assertIsNotNone(succ)
        self.assertEqual(succ.GetData(), 20)

    def test_edge_cases(self):
        self.assertIsNone(self.tree.Search(10))
        self.assertIsNone(self.tree.Successor(10))
        self.assertEqual(self.tree.Minimum(), INT_MIN)
        self.assertEqual(self.tree.Maximum(), INT_MAX)
        self.assertEqual(self.tree.Depth(10), -1)
        self.assertEqual(self.tree.Height(10), -1)
        self.tree.Delete(10)
        self.tree.InOrder()
        self.tree.PreOrder()
        self.tree.PostOrder()

    def test_duplicate_insert(self):
        self.tree.Insert(10)
        self.tree.Insert(10)
        self.assertLessEqual(self.tree.Size(), 2)

    def test_delete_root_rebalance(self):
        for v in [30, 20, 10]:
            self.tree.Insert(v)
        root = self.tree.GetRoot()
        root_data = root.GetData()
        self.tree.Delete(root_data)
        self.assertFalse(self.tree.Exists(root_data))

    def test_depth_nonexistent_key(self):
        self.tree.Insert(5)
        self.assertEqual(self.tree.Depth(999), -1)
        self.assertEqual(self.tree.Height(999), -1)

    def test_left_left_rotation(self):
        self.tree.Insert(30)
        self.tree.Insert(20)
        self.tree.Insert(10)
        root = self.tree.GetRoot()
        self.assertEqual(root.GetData(), 20)
        self.assertEqual(self.tree.Minimum(), 10)
        self.assertEqual(self.tree.Maximum(), 30)

    def test_right_right_rotation(self):
        self.tree.Insert(10)
        self.tree.Insert(20)
        self.tree.Insert(30)
        root = self.tree.GetRoot()
        self.assertEqual(root.GetData(), 20)

    def test_left_right_rotation(self):
        self.tree.Insert(30)
        self.tree.Insert(10)
        self.tree.Insert(20)
        root = self.tree.GetRoot()
        self.assertEqual(root.GetData(), 20)

    def test_right_left_rotation(self):
        self.tree.Insert(10)
        self.tree.Insert(30)
        self.tree.Insert(20)
        root = self.tree.GetRoot()
        self.assertEqual(root.GetData(), 20)

    def test_successor_chain(self):
        for v in [10, 20, 30, 40]:
            self.tree.Insert(v)
        succ = self.tree.Successor(10)
        self.assertEqual(succ.GetData(), 20)
        self.assertIsNone(self.tree.Successor(40))

    def test_large_insert(self):
        values = list(range(1, 21))
        for v in values:
            self.tree.Insert(v)
        self.assertEqual(self.tree.Size(), 20)
        self.assertEqual(self.tree.Minimum(), 1)
        self.assertEqual(self.tree.Maximum(), 20)
        for v in values:
            self.assertTrue(self.tree.Exists(v))

    def test_delete_all_nodes(self):
        values = [20, 10, 30, 5, 15, 25, 35]
        for v in values:
            self.tree.Insert(v)
        for v in values:
            self.tree.Delete(v)
        self.assertTrue(self.tree.IsEmpty())
        self.assertEqual(self.tree.Size(), 0)

    def test_min_max_after_deletions(self):
        for v in [10, 20, 30, 40, 50]:
            self.tree.Insert(v)
        self.tree.Delete(10)
        self.tree.Delete(50)
        self.assertEqual(self.tree.Minimum(), 20)
        self.assertEqual(self.tree.Maximum(), 40)

    def test_depth_of_root_is_zero(self):
        self.tree.Insert(42)
        self.assertEqual(self.tree.Depth(42), 0)

    def test_height_of_leaf_is_zero(self):
        self.tree.Insert(10)
        self.tree.Insert(5)
        self.tree.Insert(15)
        self.assertEqual(self.tree.Height(5), 0)
        self.assertEqual(self.tree.Height(15), 0)

    def test_negative_values(self):
        for v in [-10, -20, -5, -30]:
            self.tree.Insert(v)
        self.assertEqual(self.tree.Minimum(), -30)
        self.assertEqual(self.tree.Maximum(), -5)
        self.assertTrue(self.tree.Exists(-20))
        self.tree.Delete(-20)
        self.assertFalse(self.tree.Exists(-20))

if __name__ == "__main__":
    unittest.main()
