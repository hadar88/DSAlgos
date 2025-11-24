"""
Node operations for linked data structures.

This module provides Python wrappers for C++ node operations including
creation, data access, and pointer manipulation for linked lists.
"""
import os
import ctypes

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# Create
lib.Create_node.argtypes = [ctypes.c_int]
lib.Create_node.restype = ctypes.c_void_p

def Create(value):
    """
    Create a new node with the specified value.

    Args:
        value (int): The integer value to store in the node.
        
    Returns:
        ctypes.c_void_p: A pointer to the created node.
    """

    return lib.Create_node(value)

# Destroy
lib.Destroy_node.argtypes = [ctypes.c_void_p]
lib.Destroy_node.restype = None

def Destroy(node):
    """
    Destroy the node and free its memory.
    
    Args:
        node (ctypes.c_void_p): Pointer to the node to destroy.
        
    Returns:
        None
    """
    lib.Destroy_node(node)

# GetData
lib.GetData_node.argtypes = [ctypes.c_void_p]
lib.GetData_node.restype = ctypes.c_int

def GetData(node):
    """
    Get the data value stored in a node.
    
    Args:
        node (ctypes.c_void_p): Pointer to the node.

    Returns:
        int: The integer value stored in the node.
    """

    return lib.GetData_node(node)

# GetNext
lib.GetNext_node.argtypes = [ctypes.c_void_p]
lib.GetNext_node.restype = ctypes.c_void_p

def GetNext(node):
    """
    Get the next node in the linked structure.
    
    Args:
        node (ctypes.c_void_p): Pointer to the current node.

    Returns:
        ctypes.c_void_p: Pointer to the next node, or None if no next node exists.
    """

    return lib.GetNext_node(node)

# SetData
lib.SetData_node.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.SetData_node.restype = None

def SetData(node, value):
    """
    Set the data value of a node.
    
    Args:
        node (ctypes.c_void_p): Pointer to the node to modify.
        value (int): The new integer value to store in the node.
        
    Returns:
        None
    """

    lib.SetData_node(node, value)

# SetNext
lib.SetNext_node.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.SetNext_node.restype = None

def SetNext(node, next):
    """
    Set the next node pointer for a node.
    
    Args:
        node (ctypes.c_void_p): Pointer to the current node.
        next (ctypes.c_void_p): Pointer to the node that should be next, or None.

    Returns:
        None
    """

    lib.SetNext_node(node, next)