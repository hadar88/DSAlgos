from __future__ import annotations

import os
import ctypes
from ..Utils import INT_MAX, C_INT_MAX
from .LinkedList import LinkedList

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "dstructures.so"))

# --- C Library Signatures ---
lib.Create_Graph.argtypes = [ctypes.c_bool]
lib.Create_Graph.restype = ctypes.c_void_p

lib.Destroy_Graph.argtypes = [ctypes.c_void_p]
lib.Destroy_Graph.restype = None

lib.IsDirected_Graph.argtypes = [ctypes.c_void_p]
lib.IsDirected_Graph.restype = ctypes.c_bool

lib.GetSize_Graph.argtypes = [ctypes.c_void_p]
lib.GetSize_Graph.restype = ctypes.c_int

lib.CreateVertex_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.CreateVertex_Graph.restype = None

lib.DeleteVertex_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.DeleteVertex_Graph.restype = None

lib.CreateEdge_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
lib.CreateEdge_Graph.restype = None

lib.CreateWeightedEdge_Graph.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_double,
]
lib.CreateWeightedEdge_Graph.restype = None

lib.DeleteEdge_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
lib.DeleteEdge_Graph.restype = None

lib.GetNeighbors_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.GetNeighbors_Graph.restype = ctypes.c_void_p

lib.GetVertices_Graph.argtypes = [ctypes.c_void_p]
lib.GetVertices_Graph.restype = ctypes.c_void_p

lib.DisplayEdges_Graph.argtypes = [ctypes.c_void_p]
lib.DisplayEdges_Graph.restype = None

lib.Display_Graph.argtypes = [ctypes.c_void_p]
lib.Display_Graph.restype = None

lib.BFS_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.BFS_Graph.restype = ctypes.c_void_p

lib.GetBFSColor.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.GetBFSColor.restype = ctypes.c_char_p

lib.GetBFSDistance.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.GetBFSDistance.restype = ctypes.c_int

lib.GetBFSParent.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.GetBFSParent.restype = ctypes.c_int

lib.Destroy_BFSResult.argtypes = [ctypes.c_void_p]
lib.Destroy_BFSResult.restype = None

lib.GetPath_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
lib.GetPath_Graph.restype = ctypes.c_void_p

lib.Distance_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
lib.Distance_Graph.restype = ctypes.c_int

lib.GetReachableVertices_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.GetReachableVertices_Graph.restype = ctypes.c_void_p

lib.IsConnected_Graph.argtypes = [ctypes.c_void_p]
lib.IsConnected_Graph.restype = ctypes.c_bool

lib.GetTransposed_Graph.argtypes = [ctypes.c_void_p]
lib.GetTransposed_Graph.restype = ctypes.c_void_p

lib.EdgeWeight_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
lib.EdgeWeight_Graph.restype = ctypes.c_double

lib.GraphWeight_Graph.argtypes = [ctypes.c_void_p]
lib.GraphWeight_Graph.restype = ctypes.c_double

lib.Clear_Graph.argtypes = [ctypes.c_void_p]
lib.Clear_Graph.restype = None


class Graph:
    """
    Graph operations for graph data structures.

    This module provides Python wrappers for C++ Graph operations including
    creation, vertex and edge manipulation, traversal, and pathfinding. Supports
    both directed and undirected graphs with various graph algorithms.

    This module works in conjunction with the LinkedList module.
    """

    def __init__(self, directed: bool = False, ptr: ctypes.c_void_p = None) -> None:
        if ptr:
            self.ptr = ptr
        else:
            self.ptr = lib.Create_Graph(directed)

    def __del__(self) -> None:
        """Automatically destroy the graph when the object is collected."""
        if hasattr(self, "ptr") and self.ptr:
            lib.Destroy_Graph(self.ptr)
            self.ptr = None

    def IsDirected(self) -> bool:
        """Check if the graph is directed."""
        return lib.IsDirected_Graph(self.ptr)

    def GetSize(self) -> int:
        """Get the number of vertices in the graph."""
        return lib.GetSize_Graph(self.ptr)

    def CreateVertex(self, value: int) -> None:
        """Create a new vertex in the graph."""
        lib.CreateVertex_Graph(self.ptr, value)

    def DeleteVertex(self, value: int) -> None:
        """Delete a vertex from the graph."""
        lib.DeleteVertex_Graph(self.ptr, value)

    def CreateEdge(self, from_vertex: int, to_vertex: int) -> None:
        """Add an edge between two vertices in the graph."""
        lib.CreateEdge_Graph(self.ptr, from_vertex, to_vertex)

    def CreateWeightedEdge(
        self, from_vertex: int, to_vertex: int, weight: float
    ) -> None:
        """Add a weighted edge between two vertices in the graph."""
        lib.CreateWeightedEdge_Graph(self.ptr, from_vertex, to_vertex, weight)

    def DeleteEdge(self, from_vertex: int, to_vertex: int) -> None:
        """Delete an edge between two vertices in the graph."""
        lib.DeleteEdge_Graph(self.ptr, from_vertex, to_vertex)

    def GetNeighbors(self, vertex: int) -> LinkedList | None:
        """Get the neighbors of a specific vertex."""
        ll_ptr = lib.GetNeighbors_Graph(self.ptr, vertex)
        return LinkedList(ptr=ll_ptr) if ll_ptr else None

    def GetVertices(self) -> LinkedList:
        """Get all vertices in the graph."""
        ll_ptr = lib.GetVertices_Graph(self.ptr)
        return LinkedList(ptr=ll_ptr)

    def DisplayEdges(self) -> None:
        """Display all edges in the graph to console."""
        lib.DisplayEdges_Graph(self.ptr)

    def Display(self) -> None:
        """Display the graph structure to console."""
        lib.Display_Graph(self.ptr)

    def BFS(
        self, vertex: int
    ) -> tuple[dict[int, str], dict[int, int], dict[int, int | None]]:
        """Perform Breadth-First Search (BFS) on the graph."""
        res_ptr = lib.BFS_Graph(self.ptr, vertex)
        if res_ptr is None:
            return {}, {}, {}

        colors = {}
        distances = {}
        parents = {}

        try:
            ll = self.GetVertices()
            if ll:
                current = ll.GetHead()
                while current:
                    v_val = current.GetData()
                    colors[v_val] = lib.GetBFSColor(res_ptr, v_val).decode("utf-8")
                    dist = lib.GetBFSDistance(res_ptr, v_val)
                    distances[v_val] = dist if dist != C_INT_MAX else INT_MAX

                    parent_val = lib.GetBFSParent(res_ptr, v_val)
                    parents[v_val] = parent_val if parent_val != -1 else None

                    current = current.GetNext()

            return colors, distances, parents
        finally:
            lib.Destroy_BFSResult(res_ptr)

    def GetPath(self, start: int, end: int) -> LinkedList | None:
        """Get the path between two vertices."""
        ll_ptr = lib.GetPath_Graph(self.ptr, start, end)
        return LinkedList(ptr=ll_ptr) if ll_ptr else None

    def Distance(self, start: int, end: int) -> int | float:
        """Calculate the shortest distance between two vertices."""
        result = lib.Distance_Graph(self.ptr, start, end)
        return INT_MAX if result == C_INT_MAX else result

    def GetReachableVertices(self, vertex: int) -> LinkedList | None:
        """Get all vertices reachable from a specific vertex."""
        ll_ptr = lib.GetReachableVertices_Graph(self.ptr, vertex)
        return LinkedList(ptr=ll_ptr) if ll_ptr else None

    def IsConnected(self) -> bool:
        """Check if the graph is connected."""
        return lib.IsConnected_Graph(self.ptr)

    def GetTransposed(self) -> Graph | None:
        """Get the transposed graph."""
        g_ptr = lib.GetTransposed_Graph(self.ptr)
        return Graph(ptr=g_ptr) if g_ptr else None

    def EdgeWeight(self, v: int, u: int) -> float:
        """Get the weight of an edge."""
        return lib.EdgeWeight_Graph(self.ptr, v, u)

    def GraphWeight(self) -> float:
        """Get the sum of the weights of the edges."""
        return lib.GraphWeight_Graph(self.ptr)

    def Clear(self) -> None:
        """Clear all vertices and edges from the graph."""
        lib.Clear_Graph(self.ptr)
