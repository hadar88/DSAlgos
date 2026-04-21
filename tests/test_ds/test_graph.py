import unittest
from DataStructures import Graph
from DataStructures_py.Utils import INT_MAX

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.g_dir = Graph(directed=True)
        self.g_undir = Graph(directed=False)

    def tearDown(self):
        # Memory is managed by the Graph class's __del__ method
        del self.g_dir
        del self.g_undir

    def test_create_and_properties(self):
        self.assertIsNotNone(self.g_dir)
        self.assertTrue(self.g_dir.IsDirected())
        self.assertEqual(self.g_dir.GetSize(), 0)

        self.assertIsNotNone(self.g_undir)
        self.assertFalse(self.g_undir.IsDirected())

    def test_vertices(self):
        self.g_dir.CreateVertex(1)
        self.g_dir.CreateVertex(2)
        self.assertEqual(self.g_dir.GetSize(), 2)

        ll_vertices = self.g_dir.GetVertices()
        self.assertIsNotNone(ll_vertices)
        # LinkedList destruction is automatic

    def test_delete_vertex(self):
        self.g_dir.CreateVertex(1)
        self.g_dir.CreateVertex(2)
        self.g_dir.DeleteVertex(1)
        self.assertEqual(self.g_dir.GetSize(), 1)
        
        self.g_dir.DeleteVertex(99)
        self.assertEqual(self.g_dir.GetSize(), 1)

    def test_edges(self):
        self.g_undir.CreateVertex(1)
        self.g_undir.CreateVertex(2)
        self.g_undir.CreateVertex(3)

        self.g_undir.CreateEdge(1, 2)
        self.g_undir.CreateWeightedEdge(2, 3, 5.5)

        self.assertEqual(self.g_undir.EdgeWeight(2, 3), 5.5)
        self.assertEqual(self.g_undir.EdgeWeight(3, 2), 5.5)

        self.g_undir.DeleteEdge(1, 2)
        self.assertEqual(self.g_undir.EdgeWeight(1, 2), -1)

    def test_bfs_and_distance(self):
        self.g_dir.CreateVertex(1)
        self.g_dir.CreateVertex(2)
        self.g_dir.CreateVertex(3)

        self.g_dir.CreateEdge(1, 2)
        self.g_dir.CreateEdge(2, 3)

        colors, distances, parents = self.g_dir.BFS(1)
        self.assertEqual(distances.get(3), 2)
        self.assertEqual(parents.get(3), 2)

        self.assertEqual(self.g_dir.Distance(1, 3), 2)
        dist_3_1 = self.g_dir.Distance(3, 1)
        self.assertEqual(dist_3_1, INT_MAX)

    def test_get_path(self):
        self.g_dir.CreateVertex(1)
        self.g_dir.CreateVertex(2)
        self.g_dir.CreateEdge(1, 2)
        
        ll_path = self.g_dir.GetPath(1, 2)
        self.assertIsNotNone(ll_path)

        ll_invalid = self.g_dir.GetPath(1, 99)
        self.assertIsNone(ll_invalid)

    def test_connectivity_and_transpose(self):
        self.g_dir.CreateVertex(1)
        self.g_dir.CreateVertex(2)
        self.g_dir.CreateEdge(1, 2)

        self.assertFalse(self.g_dir.IsConnected())

        transposed = self.g_dir.GetTransposed()
        self.assertIsNotNone(transposed)
        # transposed is a Graph object, memory is managed

    def test_clear_and_display(self):
        self.g_dir.CreateVertex(1)
        self.g_dir.CreateVertex(2)
        self.g_dir.CreateEdge(1, 2)

        self.g_dir.Display()
        self.g_dir.DisplayEdges()

        self.g_dir.Clear()
        self.assertEqual(self.g_dir.GetSize(), 0)

    def test_edge_cases(self):
        colors, distances, parents = self.g_dir.BFS(1)
        self.assertEqual(len(colors), 0)
        
        dist = self.g_dir.Distance(1, 2)
        self.assertEqual(dist, -1)

        weight = self.g_dir.EdgeWeight(1, 2)
        self.assertEqual(weight, -1)

        self.g_dir.Clear()

    def test_get_neighbors(self):
        self.g_undir.CreateVertex(1)
        self.g_undir.CreateVertex(2)
        self.g_undir.CreateVertex(3)
        self.g_undir.CreateEdge(1, 2)
        self.g_undir.CreateEdge(1, 3)

        neighbors = self.g_undir.GetNeighbors(1)
        self.assertIsNotNone(neighbors)

        self.assertIsNone(self.g_undir.GetNeighbors(99))

    def test_undirected_edge_symmetry(self):
        self.g_undir.CreateVertex(1)
        self.g_undir.CreateVertex(2)
        self.g_undir.CreateWeightedEdge(1, 2, 7.0)
        self.assertEqual(self.g_undir.EdgeWeight(1, 2), 7.0)
        self.assertEqual(self.g_undir.EdgeWeight(2, 1), 7.0)

    def test_reachable_vertices(self):
        self.g_dir.CreateVertex(1)
        self.g_dir.CreateVertex(2)
        self.g_dir.CreateVertex(3)
        self.g_dir.CreateEdge(1, 2)
        self.g_dir.CreateEdge(2, 3)

        reachable = self.g_dir.GetReachableVertices(1)
        self.assertIsNotNone(reachable)

        r3 = self.g_dir.GetReachableVertices(3)
        self.assertEqual(r3.Size(), 0)

    def test_disconnected_graph(self):
        self.g_undir.CreateVertex(1)
        self.g_undir.CreateVertex(2)
        self.g_undir.CreateVertex(3)
        self.g_undir.CreateEdge(1, 2)
        self.assertFalse(self.g_undir.IsConnected())
        self.assertEqual(self.g_undir.Distance(1, 3), INT_MAX)

    def test_fully_connected(self):
        for v in [1, 2, 3]:
            self.g_undir.CreateVertex(v)
        self.g_undir.CreateEdge(1, 2)
        self.g_undir.CreateEdge(2, 3)
        self.assertTrue(self.g_undir.IsConnected())
        self.assertEqual(self.g_undir.Distance(1, 3), 2)

    def test_transpose_reverses_edges(self):
        for v in [1, 2, 3]:
            self.g_dir.CreateVertex(v)
        self.g_dir.CreateEdge(1, 2)
        self.g_dir.CreateEdge(2, 3)
        t = self.g_dir.GetTransposed()
        self.assertIsNotNone(t)
        self.assertNotEqual(t.EdgeWeight(2, 1), -1)
        self.assertEqual(t.EdgeWeight(1, 2), -1)

    def test_bfs_from_isolated_vertex(self):
        self.g_dir.CreateVertex(1)
        self.g_dir.CreateVertex(2)
        colors, distances, parents = self.g_dir.BFS(1)
        self.assertEqual(distances.get(2), INT_MAX)

    def test_delete_edge_removes_weight(self):
        self.g_undir.CreateVertex(1)
        self.g_undir.CreateVertex(2)
        self.g_undir.CreateWeightedEdge(1, 2, 3.5)
        self.assertEqual(self.g_undir.EdgeWeight(1, 2), 3.5)
        self.g_undir.DeleteEdge(1, 2)
        self.assertEqual(self.g_undir.EdgeWeight(1, 2), -1)

    def test_large_directed_path(self):
        for v in range(1, 11):
            self.g_dir.CreateVertex(v)
        for v in range(1, 10):
            self.g_dir.CreateEdge(v, v + 1)
        self.assertEqual(self.g_dir.GetSize(), 10)
        self.assertEqual(self.g_dir.Distance(1, 10), 9)
        self.assertEqual(self.g_dir.Distance(10, 1), INT_MAX)

if __name__ == "__main__":
    unittest.main()
