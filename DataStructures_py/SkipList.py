"""
SkipList operations for probabilistic data structures.

This module provides Python wrappers for C++ SkipList operations including
creation, insertion, deletion, and searching. Skip lists provide probabilistic
balancing with expected O(log n) performance for search, insert, and delete operations.

This module works in conjunction with the SkipListNode module.
"""
import os
import ctypes

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# Create
lib.Create_SkipList.argtypes = None
lib.Create_SkipList.restype = ctypes.c_void_p

def Create():
    """
    Create a new empty skip list.
    
    Returns:
        ctypes.c_void_p: A pointer to the skip list structure.
    """
    return lib.Create_SkipList()

# Destroy
lib.Destroy_SkipList.argtypes = [ctypes.c_void_p]
lib.Destroy_SkipList.restype = None

def Destroy(skipList):
    """
    Destroy the skip list and free its memory.

    Args:
        skipList (ctypes.c_void_p): Pointer to the skip list structure.

    Returns:
        None
    """
    if skipList:
        lib.Destroy_SkipList(skipList)

# IsEmpty
lib.IsEmpty_SkipList.argtypes = [ctypes.c_void_p]
lib.IsEmpty_SkipList.restype = ctypes.c_bool

def IsEmpty(skipList):
    """
    Check if the skip list is empty.
    
    Args:
        skipList (ctypes.c_void_p): Pointer to the skip list structure.

    Returns:
        bool: True if the skip list is empty (no nodes), False otherwise.
    """
    return lib.IsEmpty_SkipList(skipList)

# GetHead
lib.GetHead_SkipList.argtypes = [ctypes.c_void_p]
lib.GetHead_SkipList.restype = ctypes.c_void_p

def GetHead(skipList):
    """
    Get the head node of the skip list.
    
    Args:
        skipList (ctypes.c_void_p): Pointer to the skip list structure.

    Returns:
        ctypes.c_void_p: Pointer to the head SkipListNode, or None if list is empty.
    """
    return lib.GetHead_SkipList(skipList)

# GetHeight
lib.GetHeight_SkipList.argtypes = [ctypes.c_void_p]
lib.GetHeight_SkipList.restype = ctypes.c_int

def GetHeight(skipList):
    """
    Get the current height of the skip list.
    
    Args:
        skipList (ctypes.c_void_p): Pointer to the skip list structure.

    Returns:
        int: The maximum height of any node in the skip list.
    """
    return lib.GetHeight_SkipList(skipList)

# Search
lib.Search_SkipList.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Search_SkipList.restype = ctypes.c_void_p

def Search(skipList, key):
    """
    Search for a key in the skip list and return the node.
    
    Args:
        skipList (ctypes.c_void_p): Pointer to the skip list structure.
        key (int): The value to search for.
        
    Returns:
        ctypes.c_void_p: Pointer to the SkipListNode containing the key, or None if not found.
    """
    return lib.Search_SkipList(skipList, key)

# Insert
lib.Insert_SkipList.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Insert_SkipList.restype = None

def Insert(skipList, key):
    """
    Insert a new key into the skip list with probabilistic height assignment.
    
    Args:
        skipList (ctypes.c_void_p): Pointer to the skip list structure.
        key (int): The value to insert.
        
    Returns:
        None
    """
    lib.Insert_SkipList(skipList, key)

# Delete
lib.Delete_SkipList.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Delete_SkipList.restype = None

def Delete(skipList, key):
    """
    Delete a key from the skip list.
    
    Args:
        skipList (ctypes.c_void_p): Pointer to the skip list structure.
        key (int): The value to delete.
        
    Returns:
        None
    """
    lib.Delete_SkipList(skipList, key)

# Display
lib.Display_SkipList.argtypes = [ctypes.c_void_p]
lib.Display_SkipList.restype = None

def Display(skipList):
    """
    Display all elements in the skip list to console.
    
    Args:
        skipList (ctypes.c_void_p): Pointer to the skip list structure.

    Returns:
        None
    """
    lib.Display_SkipList(skipList)