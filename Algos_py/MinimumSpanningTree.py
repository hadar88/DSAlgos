"""
Minimum Spanning Tree algorithms.

This module provides Python wrappers for C++ MST algorithms, including
Kruskal's algorithm.
"""
import os
import ctypes
from DataStructures import Graph

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/algos.so"))

# --- C Library Signatures ---
lib.Kruskal.argtypes = [ctypes.c_void_p]
lib.Kruskal.restype = ctypes.c_void_p

class MinimumSpanningTree:
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
        - Time complexity: O(E log V)
        """
        if not graph:
            return None
        
        mst_ptr = lib.Kruskal(graph.ptr)
        return Graph(ptr=mst_ptr) if mst_ptr else None