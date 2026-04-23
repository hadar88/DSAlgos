import unittest
from DataStructures import SkipListNode

class TestSkipListNode(unittest.TestCase):
    def test_create_and_destroy(self):
        node = SkipListNode(10, 3)
        self.assertIsNotNone(node)
        self.assertEqual(node.GetData(), 10)
        self.assertEqual(node.GetHeight(), 3)

    def test_set_data_and_height(self):
        node = SkipListNode(5, 1)
        node.SetData(20)
        node.SetHeight(5)
        
        self.assertEqual(node.GetData(), 20)
        self.assertEqual(node.GetHeight(), 5)

    def test_pointers(self):
        node1 = SkipListNode(1, 2)
        node2 = SkipListNode(2, 2)
        
        node1.SetNext(0, node2)
        node2.SetPrev(0, node1)

        next_node = node1.GetNext(0)
        prev_node = node2.GetPrev(0)

        self.assertIsNotNone(next_node)
        self.assertIsNotNone(prev_node)
        
        self.assertEqual(next_node.GetData(), 2)
        self.assertEqual(prev_node.GetData(), 1)

if __name__ == "__main__":
    unittest.main()
