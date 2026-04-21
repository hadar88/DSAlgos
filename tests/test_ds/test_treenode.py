import unittest
from DataStructures import TreeNode

class TestTreeNode(unittest.TestCase):
    def test_create_and_empty(self):
        node = TreeNode(100)
        self.assertIsNotNone(node)
        self.assertEqual(node.GetData(), 100)

    def test_pointers(self):
        root = TreeNode(10)
        left = TreeNode(5)
        right = TreeNode(15)

        root.SetLeft(left)
        root.SetRight(right)
        left.SetParent(root)
        right.SetParent(root)

        left_child = root.GetLeft()
        right_child = root.GetRight()

        self.assertIsNotNone(left_child)
        self.assertIsNotNone(right_child)

        self.assertEqual(left_child.GetData(), 5)
        self.assertEqual(right_child.GetData(), 15)

        self.assertEqual(left.GetParent().GetData(), 10)
        self.assertEqual(right.GetParent().GetData(), 10)

    def test_fresh_node_has_null_pointers(self):
        node = TreeNode(99)
        self.assertIsNone(node.GetLeft())
        self.assertIsNone(node.GetRight())
        self.assertIsNone(node.GetParent())

    def test_set_and_get_data_mutation(self):
        node = TreeNode(1)
        for v in [0, -1, 100]:
            node.SetData(v)
            self.assertEqual(node.GetData(), v)

    def test_detach_child(self):
        root = TreeNode(10)
        left = TreeNode(5)
        root.SetLeft(left)
        self.assertIsNotNone(root.GetLeft())
        root.SetLeft(None)
        self.assertIsNone(root.GetLeft())

    def test_relink_children(self):
        root = TreeNode(10)
        a = TreeNode(5)
        b = TreeNode(7)
        root.SetLeft(a)
        self.assertEqual(root.GetLeft().GetData(), 5)
        root.SetLeft(b)
        self.assertEqual(root.GetLeft().GetData(), 7)

    def test_negative_and_boundary_data(self):
        for v in [-1, 0, 1]:
            node = TreeNode(v)
            self.assertEqual(node.GetData(), v)
