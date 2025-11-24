"""
LinkedList operations for dynamic data structures.

This module provides Python wrappers for C++ linked list operations including
creation, insertion, deletion, and traversal. The linked list implementation
supports dynamic memory allocation and efficient insertion/deletion operations.
"""
import os
import ctypes

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# Create
lib.Create_linkedlist.argtypes = []
lib.Create_linkedlist.restype = ctypes.c_void_p

def Create():
    """
    Create a new empty linked list.
    
    Returns:
        ctypes.c_void_p: A pointer to the linked list structure (pointer to head pointer).
    """
    return lib.Create_linkedlist()

# Destroy
lib.Destroy_linkedlist.argtypes = [ctypes.c_void_p]
lib.Destroy_linkedlist.restype = None
def Destroy(linked_list):
    """
    Destroy the linked list and free its memory.
    
    Args:
        linked_list (ctypes.c_void_p): Pointer to the linked list structure.
        
    Returns:
        None
    """
    lib.Destroy_linkedlist(linked_list)

# GetHead
lib.GetHead_linkedlist.argtypes = [ctypes.c_void_p]
lib.GetHead_linkedlist.restype = ctypes.c_void_p

def GetHead(linked_list):
    """
    Get the head node of the linked list.
    
    Args:
        linked_list (ctypes.c_void_p): Pointer to the linked list structure.

    Returns:
        ctypes.c_void_p: Pointer to the first node in the list, or None if list is empty.
    """
    return lib.GetHead_linkedlist(linked_list)

# Insert
lib.Insert_linkedlist.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Insert_linkedlist.restype = None

def Insert(linked_list, value):
    """
    Insert a new value at the beginning of the linked list.
    
    Args:
        linked_list (ctypes.c_void_p): Pointer to the linked list structure.
        value (int): The integer value to insert.
        
    Returns:
        None
    """
    lib.Insert_linkedlist(linked_list, value)

# InsertLast
lib.InsertLast_linkedlist.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.InsertLast_linkedlist.restype = None

def InsertLast(linked_list, value):
    """
    Insert a new value at the end of the linked list.
    
    Args:
        linked_list (ctypes.c_void_p): Pointer to the linked list structure.
        value (int): The integer value to insert.
        
    Returns:
        None
    """
    lib.InsertLast_linkedlist(linked_list, value)

# Delete
lib.Delete_linkedlist.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Delete_linkedlist.restype = None

def Delete(linked_list, value):
    """
    Delete the first occurrence of a value from the linked list.
    
    Args:
        linked_list (ctypes.c_void_p): Pointer to the linked list structure.
        value (int): The integer value to delete.
        
    Returns:
        None
    """
    lib.Delete_linkedlist(linked_list, value)

# IsEmpty
lib.IsEmpty_linkedlist.argtypes = [ctypes.c_void_p]
lib.IsEmpty_linkedlist.restype = ctypes.c_bool

def IsEmpty(linked_list):
    """
    Check if the linked list is empty.
    
    Args:
        linked_list (ctypes.c_void_p): Pointer to the linked list structure.

    Returns:
        bool: True if the list is empty (no nodes), False otherwise.
    """
    return lib.IsEmpty_linkedlist(linked_list)

# Display
lib.Display_linkedlist.argtypes = [ctypes.c_void_p]
lib.Display_linkedlist.restype = None

def Display(linked_list):
    """
    Display all elements in the linked list to console.
    
    Args:
        linked_list (ctypes.c_void_p): Pointer to the linked list structure.

    Returns:
        None
    """
    lib.Display_linkedlist(linked_list)