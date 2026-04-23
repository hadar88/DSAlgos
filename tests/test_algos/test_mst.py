import unittest
from Algos import MST
from DataStructures import Graph

class TestMST(unittest.TestCase):
    def test_kruskal_standard(self):
        g = Graph(directed=False)
        for i in range(4):
            g.CreateVertex(i)
        
        g.CreateWeightedEdge(0, 1, 10.0)
        g.CreateWeightedEdge(0, 2, 6.0)
        g.CreateWeightedEdge(0, 3, 5.0)
        g.CreateWeightedEdge(1, 3, 15.0)
        g.CreateWeightedEdge(2, 3, 4.0)

        mst = MST.Kruskal(g)
        
        self.assertIsNotNone(mst)
        self.assertEqual(mst.GetSize(), 4)
        
        self.assertTrue(mst.IsConnected())
        
        self.assertEqual(mst.EdgeWeight(2, 3), 4.0)
        self.assertEqual(mst.EdgeWeight(0, 3), 5.0)
        self.assertEqual(mst.EdgeWeight(0, 1), 10.0)
        
        self.assertEqual(mst.EdgeWeight(0, 2), -1.0)

    def test_kruskal_empty(self):
        self.assertIsNone(MST.Kruskal(None))
        
        g = Graph(directed=False)
        mst = MST.Kruskal(g)
        self.assertIsNotNone(mst)
        self.assertEqual(mst.GetSize(), 0)

    def test_kruskal_single_vertex(self):
        g = Graph(directed=False)
        g.CreateVertex(1)
        mst = MST.Kruskal(g)
        self.assertIsNotNone(mst)
        self.assertEqual(mst.GetSize(), 1)

    def test_kruskal_disconnected(self):
        g = Graph(directed=False)
        g.CreateVertex(1)
        g.CreateVertex(2)
        g.CreateVertex(3)
        g.CreateVertex(4)
        g.CreateWeightedEdge(1, 2, 1.0)
        g.CreateWeightedEdge(3, 4, 2.0)
        
        mst = MST.Kruskal(g)
        self.assertIsNone(mst)

    def test_prim_standard(self):
        g = Graph(directed=False)
        for i in range(4):
            g.CreateVertex(i)
        
        g.CreateWeightedEdge(0, 1, 10.0)
        g.CreateWeightedEdge(0, 2, 6.0)
        g.CreateWeightedEdge(0, 3, 5.0)
        g.CreateWeightedEdge(1, 3, 15.0)
        g.CreateWeightedEdge(2, 3, 4.0)

        mst = MST.Prim(g)
        
        self.assertIsNotNone(mst)
        self.assertEqual(mst.GetSize(), 4)
        
        self.assertTrue(mst.IsConnected())
        
        self.assertEqual(mst.EdgeWeight(2, 3), 4.0)
        self.assertEqual(mst.EdgeWeight(0, 3), 5.0)
        self.assertEqual(mst.EdgeWeight(0, 1), 10.0)
        
        self.assertEqual(mst.EdgeWeight(0, 2), -1.0)

    def test_prim_empty(self):
        self.assertIsNone(MST.Prim(None))
        
        g = Graph(directed=False)
        mst = MST.Prim(g)
        self.assertIsNotNone(mst)
        self.assertEqual(mst.GetSize(), 0)

    def test_prim_single_vertex(self):
        g = Graph(directed=False)
        g.CreateVertex(1)
        mst = MST.Prim(g)
        self.assertIsNotNone(mst)
        self.assertEqual(mst.GetSize(), 1)

    def test_prim_disconnected(self):
        g = Graph(directed=False)
        g.CreateVertex(1)
        g.CreateVertex(2)
        g.CreateVertex(3)
        g.CreateVertex(4)
        g.CreateWeightedEdge(1, 2, 1.0)
        g.CreateWeightedEdge(3, 4, 2.0)
        
        mst = MST.Prim(g)
        self.assertIsNone(mst)

if __name__ == "__main__":
    unittest.main()
