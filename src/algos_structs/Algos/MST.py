"""
Minimum Spanning Tree algorithms.

This module provides Python wrappers for C++ MST algorithms, including
Kruskal's algorithm.
"""
import os
import ctypes
from ..DataStructures.Graph import Graph

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "algos.so"))

# --- C Library Signatures ---
lib.Kruskal.argtypes = [ctypes.c_void_p]
lib.Kruskal.restype = ctypes.c_void_p

lib.Prim.argtypes = [ctypes.c_void_p]
lib.Prim.restype = ctypes.c_void_p

class MST:
    """A collection of Minimum Spanning Tree algorithms."""

    @staticmethod
    def Kruskal(graph: Graph) -> Graph | None:
        """
        Find a Minimum Spanning Tree using Kruskal's algorithm.

        Parameters
        ----------
        graph : Graph
            The input graph.

        Returns
        -------
        Graph
            The Minimum Spanning Tree.

        Notes
        -----
        - Time complexity: Best: O(E + alpha(V)) when the edges are already sorted, Average: O(E log V)
        """
        if not graph:
            return None
        
        mst_ptr = lib.Kruskal(graph.ptr)
        return Graph(ptr=mst_ptr) if mst_ptr else None

    @staticmethod
    def Prim(graph: Graph) -> Graph | None:
        """
        Find a Minimum Spanning Tree using Prim's algorithm.

        Parameters
        ----------
        graph : Graph
            The input graph.

        Returns
        -------
        Graph
            The Minimum Spanning Tree.

        Notes
        -----
        - Time complexity: Best: O(E log V)
        """
        if not graph:
            return None

        mst_ptr = lib.Prim(graph.ptr)
        return Graph(ptr=mst_ptr) if mst_ptr else None