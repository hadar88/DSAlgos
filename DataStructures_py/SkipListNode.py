"""
SkipListNode operations for skip list data structures.

This module provides Python wrappers for C++ SkipListNode operations including
creation, data access, and navigation through multiple levels. Skip list nodes
support probabilistic data structure operations with multiple forward/backward pointers.
"""
import os
import ctypes

INT_MIN = -2147483648  # Minimum value for a 32-bit signed integer

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# Create
lib.Create_SkipListNode.argtypes = [ctypes.c_int, ctypes.c_int]
lib.Create_SkipListNode.restype = ctypes.c_void_p

def Create(value, height):
    """
    Create a new skip list node with the specified value and height.
    
    Args:
        value (int): The integer value to store in the node.
        height (int): The height (number of levels) for this node.
        
    Returns:
        ctypes.c_void_p: A pointer to the created skip list node.
    """
    return lib.Create_SkipListNode(value, height)

# Destroy   
lib.Destroy_SkipListNode.argtypes = [ctypes.c_void_p]
lib.Destroy_SkipListNode.restype = None

def Destroy(node):
    """
    Destroy the skip list node and free its memory.
    
    Args:
        node (ctypes.c_void_p): Pointer to the skip list node to destroy.
        
    Returns:
        None
    """
    lib.Destroy_SkipListNode(node)

# GetData
lib.GetData_SkipListNode.argtypes = [ctypes.c_void_p]
lib.GetData_SkipListNode.restype = ctypes.c_int

def GetData(node):
    """
    Get the data value stored in a skip list node.
    
    Args:
        node (ctypes.c_void_p): Pointer to the skip list node.

    Returns:
        int: The integer value stored in the node.
    """
    data = lib.GetData_SkipListNode(node)
    if(data != INT_MIN):
        return data

# GetHeight
lib.GetHeight_SkipListNode.argtypes = [ctypes.c_void_p]
lib.GetHeight_SkipListNode.restype = ctypes.c_int

def GetHeight(node):
    """
    Get the height (number of levels) of a skip list node.
    
    Args:
        node (ctypes.c_void_p): Pointer to the skip list node.

    Returns:
        int: The height of the node.
    """
    return lib.GetHeight_SkipListNode(node)

# GetNext
lib.GetNext_SkipListNode.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.GetNext_SkipListNode.restype = ctypes.c_void_p

def GetNext(node, level):
    """
    Get the next node at a specific level in the skip list.
    
    Args:
        node (ctypes.c_void_p): Pointer to the current skip list node.
        level (int): The level to get the next node from (0-based).
        
    Returns:
        ctypes.c_void_p: Pointer to the next node at the specified level, or None if no next node.
    """
    return lib.GetNext_SkipListNode(node, level)

# GetPrev
lib.GetPrev_SkipListNode.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.GetPrev_SkipListNode.restype = ctypes.c_void_p

def GetPrev(node, level):
    """
    Get the previous node at a specific level in the skip list.
    
    Args:
        node (ctypes.c_void_p): Pointer to the current skip list node.
        level (int): The level to get the previous node from (0-based).
        
    Returns:
        ctypes.c_void_p: Pointer to the previous node at the specified level, or None if no previous node.
    """
    return lib.GetPrev_SkipListNode(node, level)

# SetData
lib.SetData_SkipListNode.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.SetData_SkipListNode.restype = None

def SetData(node, data):
    """
    Set the data value of a skip list node.
    
    Args:
        node (ctypes.c_void_p): Pointer to the skip list node to modify.
        data (int): The new integer value to store in the node.
        
    Returns:
        None
    """
    lib.SetData_SkipListNode(node, data)

# SetHeight
lib.SetHeight_SkipListNode.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.SetHeight_SkipListNode.restype = None

def SetHeight(node, height):
    """
    Set the height (number of levels) of a skip list node.
    
    Args:
        node (ctypes.c_void_p): Pointer to the skip list node to modify.
        height (int): The new height for the node.
        
    Returns:
        None
    """
    lib.SetHeight_SkipListNode(node, height)

# SetNext
lib.SetNext_SkipListNode.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
lib.SetNext_SkipListNode.restype = None

def SetNext(node, level, next):
    """
    Set the next node pointer at a specific level in the skip list.
    
    Args:
        node (ctypes.c_void_p): Pointer to the current skip list node.
        level (int): The level to set the next node pointer (0-based).
        next (ctypes.c_void_p): Pointer to the node that should be next at this level, or None.

    Returns:
        None
    """
    lib.SetNext_SkipListNode(node, level, next)

# SetPrev
lib.SetPrev_SkipListNode.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
lib.SetPrev_SkipListNode.restype = None

def SetPrev(node, level, prev):
    """
    Set the previous node pointer at a specific level in the skip list.
    
    Args:
        node (ctypes.c_void_p): Pointer to the current skip list node.
        level (int): The level to set the previous node pointer (0-based).
        prev (ctypes.c_void_p): Pointer to the node that should be previous at this level, or None.

    Returns:
        None
    """
    lib.SetPrev_SkipListNode(node, level, prev)