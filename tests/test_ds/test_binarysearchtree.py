import unittest
from DataStructures import BinarySearchTree
from DataStructures_py.Utils import INT_MAX, INT_MIN

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()

    def test_create_and_empty(self):
        self.assertIsNotNone(self.tree)
        self.assertTrue(self.tree.IsEmpty())
        self.assertEqual(self.tree.Size(), 0)
        self.assertIsNone(self.tree.GetRoot())

    def test_insert_and_search(self):
        self.tree.Insert(50)
        self.tree.Insert(30)
        self.tree.Insert(70)
        
        self.assertEqual(self.tree.Size(), 3)
        self.assertFalse(self.tree.IsEmpty())

        self.assertTrue(self.tree.Exists(30))
        self.assertFalse(self.tree.Exists(99))

        node = self.tree.Search(70)
        self.assertIsNotNone(node)
        self.assertEqual(node.GetData(), 70)

    def test_min_max(self):
        self.tree.Insert(10)
        self.tree.Insert(5)
        self.tree.Insert(20)
        self.assertEqual(self.tree.Minimum(), 5)
        self.assertEqual(self.tree.Maximum(), 20)

    def test_delete(self):
        self.tree.Insert(50)
        self.tree.Insert(30)
        self.tree.Insert(70)
        self.tree.Delete(30)
        self.assertEqual(self.tree.Size(), 2)
        self.assertFalse(self.tree.Exists(30))

    def test_successor(self):
        self.tree.Insert(50)
        self.tree.Insert(30)
        self.tree.Insert(70)
        self.tree.Insert(40)
        
        node = self.tree.Successor(30)
        self.assertIsNotNone(node)
        self.assertEqual(node.GetData(), 40)
        
        node = self.tree.Successor(70)
        self.assertIsNone(node)

    def test_depth_height(self):
        self.tree.Insert(50)
        self.tree.Insert(30)
        self.tree.Insert(70)
        self.tree.Insert(20)
        
        self.assertEqual(self.tree.Depth(50), 0)
        self.assertEqual(self.tree.Depth(20), 2)
        self.assertEqual(self.tree.Height(50), 2)
        self.assertEqual(self.tree.Height(30), 1)

    def test_traversals(self):
        self.tree.Insert(10)
        self.tree.Insert(5)
        self.tree.Insert(15)
        self.tree.InOrder()
        self.tree.PreOrder()
        self.tree.PostOrder()

    def test_empty_min_max(self):
        self.assertEqual(self.tree.Minimum(), INT_MIN)
        self.assertEqual(self.tree.Maximum(), INT_MAX)

    def test_search_non_existent(self):
        self.tree.Insert(10)
        self.assertIsNone(self.tree.Search(99))
        self.assertIsNone(self.tree.Successor(10))

    def test_large_tree(self):
        for i in range(1, 51):
            self.tree.Insert(i)
        self.assertEqual(self.tree.Size(), 50)
        self.assertEqual(self.tree.Maximum(), 50)
        self.assertEqual(self.tree.Minimum(), 1)
