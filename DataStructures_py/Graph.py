"""
Graph operations for graph data structures.

This module provides Python wrappers for C++ Graph operations including
creation, vertex and edge manipulation, traversal, and pathfinding. Supports
both directed and undirected graphs with various graph algorithms.

This module works in conjunction with the LinkedList module.
"""
import os
import ctypes

INT_MAX = 2147483647 # Maximum value for a 32-bit signed integer

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# Create
lib.Create_Graph.argtypes = [ctypes.c_bool]
lib.Create_Graph.restype = ctypes.c_void_p

def Create(directed):
    """
    Create a new graph structure.
    
    Args:
        directed (bool): True to create a directed graph, False for undirected.
        
    Returns:
        ctypes.c_void_p: A pointer to the graph structure.
    """
    return lib.Create_Graph(directed)

# Destroy
lib.Destroy_Graph.argtypes = [ctypes.c_void_p]
lib.Destroy_Graph.restype = None

def Destroy(graph):
    """
    Destroy the graph and free its memory.

    Args:
        graph (ctypes.c_void_p): Pointer to the graph structure.

    Returns:
        None
    """
    if graph:
        lib.Destroy_Graph(graph)

# IsDirected
lib.IsDirected_Graph.argtypes = [ctypes.c_void_p]
lib.IsDirected_Graph.restype = ctypes.c_bool

def IsDirected(graph):
    """
    Check if the graph is directed.
    
    Args:
        graph (ctypes.c_void_p): Pointer to the graph structure.
        
    Returns:
        bool: True if the graph is directed, False if undirected.
    """
    return lib.IsDirected_Graph(graph)

# GetSize
lib.GetSize_Graph.argtypes = [ctypes.c_void_p]
lib.GetSize_Graph.restype = ctypes.c_int

def GetSize(graph):
    """
    Get the number of vertices in the graph.
    
    Args:
        graph (ctypes.c_void_p): Pointer to the graph structure.
        
    Returns:
        int: The number of vertices in the graph.
    """
    return lib.GetSize_Graph(graph)

# CreateVertex
lib.CreateVertex_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.CreateVertex_Graph.restype = None

def CreateVertex(graph, value):
    """
    Create a new vertex in the graph.
    
    Args:
        graph (ctypes.c_void_p): Pointer to the graph structure.
        value (int): The integer value for the new vertex.
        
    Returns:
        None
    """
    lib.CreateVertex_Graph(graph, value)

# DeleteVertex
lib.DeleteVertex_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.DeleteVertex_Graph.restype = None

def DeleteVertex(graph, value):
    """
    Delete a vertex from the graph.
    
    Args:
        graph (ctypes.c_void_p): Pointer to the graph structure.
        value (int): The value of the vertex to delete.
        
    Returns:
        None
    """
    lib.DeleteVertex_Graph(graph, value)

# AddEdge
lib.AddEdge_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
lib.AddEdge_Graph.restype = None

def AddEdge(graph, from_vertex, to_vertex):
    """
    Add an edge between two vertices in the graph.
    
    Args:
        graph (ctypes.c_void_p): Pointer to the graph structure.
        from_vertex (int): The source vertex value.
        to_vertex (int): The destination vertex value.
        
    Returns:
        None
    """
    lib.AddEdge_Graph(graph, from_vertex, to_vertex)

# DeleteEdge
lib.DeleteEdge_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
lib.DeleteEdge_Graph.restype = None

def DeleteEdge(graph, from_vertex, to_vertex):
    """
    Delete an edge between two vertices in the graph.
    
    Args:
        graph (ctypes.c_void_p): Pointer to the graph structure.
        from_vertex (int): The source vertex value.
        to_vertex (int): The destination vertex value.
        
    Returns:
        None
    """
    lib.DeleteEdge_Graph(graph, from_vertex, to_vertex)

# GetNeighbors
lib.GetNeighbors_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.GetNeighbors_Graph.restype = ctypes.c_void_p

def GetNeighbors(graph, vertex):
    """
    Get the neighbors of a specific vertex.
    
    Args:
        graph (ctypes.c_void_p): Pointer to the graph structure.
        vertex (int): The vertex value to get neighbors for.
        
    Returns:
        ctypes.c_void_p: Pointer to a LinkedList containing neighbor vertices, or None if no neighbors.
    """
    result = lib.GetNeighbors_Graph(graph, vertex)
    if result:
        return result

# GetVertices
lib.GetVertices_Graph.argtypes = [ctypes.c_void_p]
lib.GetVertices_Graph.restype = ctypes.c_void_p

def GetVertices(graph):
    """
    Get all vertices in the graph.
    
    Args:
        graph (ctypes.c_void_p): Pointer to the graph structure.
        
    Returns:
        ctypes.c_void_p: Pointer to a LinkedList containing all vertices, or None if graph is empty.
    """
    result = lib.GetVertices_Graph(graph)
    if result:
        return result
    return None

# DisplayEdges
lib.DisplayEdges_Graph.argtypes = [ctypes.c_void_p]
lib.DisplayEdges_Graph.restype = None

def DisplayEdges(graph):
    """
    Display all edges in the graph to console.
    
    Args:
        graph (ctypes.c_void_p): Pointer to the graph structure.
        
    Returns:
        None
    """
    lib.DisplayEdges_Graph(graph)

# Display
lib.Display_Graph.argtypes = [ctypes.c_void_p]
lib.Display_Graph.restype = None

def Display(graph):
    """
    Display the graph structure to console.
    
    Args:
        graph (ctypes.c_void_p): Pointer to the graph structure.
        
    Returns:
        None
    """
    lib.Display_Graph(graph)

# PrintPath
lib.PrintPath_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
lib.PrintPath_Graph.restype = None

def PrintPath(graph, start, end):
    """
    Print the path between two vertices to console.
    
    Args:
        graph (ctypes.c_void_p): Pointer to the graph structure.
        start (int): The starting vertex value.
        end (int): The ending vertex value.
        
    Returns:
        None
    """
    lib.PrintPath_Graph(graph, start, end)

# Distance
lib.Distance_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
lib.Distance_Graph.restype = ctypes.c_int

def Distance(graph, start, end):
    """
    Calculate the shortest distance between two vertices.
    
    Args:
        graph (ctypes.c_void_p): Pointer to the graph structure.
        start (int): The starting vertex value.
        end (int): The ending vertex value.
        
    Returns:
        int or str: The shortest distance between vertices, or a message if unreachable.
    """
    result = lib.Distance_Graph(graph, start, end)
    if result == INT_MAX:
        return f"Vertex {end} is unreachable from vertex {start}"
    if result != -1:
        return result

# GetReachableVertices
lib.GetReachableVertices_Graph.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.GetReachableVertices_Graph.restype = ctypes.c_void_p

def GetReachableVertices(graph, vertex):
    """
    Get all vertices reachable from a specific vertex.
    
    Args:
        graph (ctypes.c_void_p): Pointer to the graph structure.
        vertex (int): The starting vertex value.
        
    Returns:
        ctypes.c_void_p: Pointer to a LinkedList containing reachable vertices, or None if none reachable.
    """
    result = lib.GetReachableVertices_Graph(graph, vertex)
    if result:
        return result
    
# Clear
lib.Clear_Graph.argtypes = [ctypes.c_void_p]
lib.Clear_Graph.restype = None

def Clear(graph):
    """
    Clear all vertices and edges from the graph.
    
    Args:
        graph (ctypes.c_void_p): Pointer to the graph structure.
        
    Returns:
        None
    """
    lib.Clear_Graph(graph)

# Destroy returned linked list
lib.Destroy_linkedlist.argtypes = [ctypes.c_void_p]
lib.Destroy_linkedlist.restype = None

def DestroyReturnedLinkedList(linked_list):
    """
    Destroy a linked list returned from another function and free its memory.

    Args:
        linked_list (ctypes.c_void_p): Pointer to the linked list structure.

    Returns:
        None
    """
    if linked_list:
        lib.Destroy_linkedlist(linked_list)
