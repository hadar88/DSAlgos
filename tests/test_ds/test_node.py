import unittest
from DataStructures import Node

class TestNode(unittest.TestCase):
    def test_create_and_destroy(self):
        node = Node(42)
        self.assertIsNotNone(node)
        self.assertEqual(node.GetData(), 42)

    def test_get_and_set_data(self):
        node = Node(10)
        self.assertEqual(node.GetData(), 10)
        node.SetData(20)
        self.assertEqual(node.GetData(), 20)

    def test_get_and_set_next(self):
        node1 = Node(1)
        node2 = Node(2)
        
        self.assertIsNone(node1.GetNext())
        
        node1.SetNext(node2)
        next_node = node1.GetNext()
        
        self.assertIsNotNone(next_node)
        self.assertEqual(next_node.GetData(), 2)
        
    def test_overwrite_data(self):
        node = Node(100)
        node.SetData(-1)
        self.assertEqual(node.GetData(), -1)
        node.SetData(0)
        self.assertEqual(node.GetData(), 0)

    def test_chain_nodes(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        a.SetNext(b)
        b.SetNext(c)
        self.assertEqual(a.GetNext().GetNext().GetData(), 3)
        self.assertIsNone(c.GetNext())

    def test_detach_next(self):
        a = Node(1)
        b = Node(2)
        a.SetNext(b)
        self.assertIsNotNone(a.GetNext())
        a.SetNext(None)
        self.assertIsNone(a.GetNext())

    def test_negative_and_boundary_data(self):
        for v in [-1, 0, 1]:
            node = Node(v)
            self.assertEqual(node.GetData(), v)
    
    def test_long_chain(self):
        nodes = [Node(i) for i in range(10)]
        for i in range(9):
            nodes[i].SetNext(nodes[i + 1])
        cur = nodes[0]
        for i in range(10):
            self.assertEqual(cur.GetData(), i)
            cur = cur.GetNext()
        self.assertIsNone(cur)
        