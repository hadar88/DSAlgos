"""
PriorityQueue operations for heap-based priority queue data structures.

This module provides Python wrappers for C++ PriorityQueue operations including
creation, insertion, extraction, and heap operations. The priority queue is implemented
as a max-heap where the highest priority (maximum value) element is at the root.
"""
import os
import ctypes

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# Create
lib.Create_PriorityQueue.argtypes = []
lib.Create_PriorityQueue.restype = ctypes.c_void_p

def Create():
    """
    Create a new empty priority queue.
    
    Returns:
        ctypes.c_void_p: A pointer to the priority queue structure.
    """
    return lib.Create_PriorityQueue()

# Destroy
lib.Destroy_PriorityQueue.argtypes = [ctypes.c_void_p]
lib.Destroy_PriorityQueue.restype = None

def Destroy(pq):
    """
    Destroy the priority queue and free its memory.

    Args:
        pq (ctypes.c_void_p): Pointer to the priority queue structure.

    Returns:
        None
    """
    if pq:
        lib.Destroy_PriorityQueue(pq)

# GetSize
lib.GetSize_PriorityQueue.argtypes = [ctypes.c_void_p]
lib.GetSize_PriorityQueue.restype = ctypes.c_int

def GetSize(pq):
    """
    Get the number of elements in the priority queue.
    
    Args:
        pq (ctypes.c_void_p): Pointer to the priority queue structure.
        
    Returns:
        int: The number of elements currently in the priority queue.
    """
    return lib.GetSize_PriorityQueue(pq)

# Maximum
lib.Maximum_PriorityQueue.argtypes = [ctypes.c_void_p]
lib.Maximum_PriorityQueue.restype = ctypes.c_int

def Maximum(pq):
    """
    Get the maximum element (highest priority) from the priority queue.
    
    Args:
        pq (ctypes.c_void_p): Pointer to the priority queue structure.
        
    Returns:
        int: The maximum value in the priority queue.
    """
    return lib.Maximum_PriorityQueue(pq)

# ExtractMax
lib.ExtractMax_PriorityQueue.argtypes = [ctypes.c_void_p]
lib.ExtractMax_PriorityQueue.restype = ctypes.c_int

def ExtractMax(pq):
    """
    Remove and return the maximum element from the priority queue.
    
    Args:
        pq (ctypes.c_void_p): Pointer to the priority queue structure.
        
    Returns:
        int: The maximum value that was removed from the priority queue.
    """
    return lib.ExtractMax_PriorityQueue(pq)

# IncreaseKey
lib.IncreaseKey_PriorityQueue.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
lib.IncreaseKey_PriorityQueue.restype = None

def IncreaseKey(pq, index, value):
    """
    Increase the priority of an element at a specific index.
    
    Args:
        pq (ctypes.c_void_p): Pointer to the priority queue structure.
        index (int): The index of the element to modify (0-based).
        value (int): The new higher value to assign to the element.
        
    Returns:
        None
    """
    lib.IncreaseKey_PriorityQueue(pq, index, value)

# Insert
lib.Insert_PriorityQueue.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Insert_PriorityQueue.restype = None

def Insert(pq, value):
    """
    Insert a new element into the priority queue.
    
    Args:
        pq (ctypes.c_void_p): Pointer to the priority queue structure.
        value (int): The integer value to insert.
        
    Returns:
        None
    """
    lib.Insert_PriorityQueue(pq, value)

# HeapSort
lib.HeapSort_PriorityQueue.argtypes = [ctypes.c_void_p]
lib.HeapSort_PriorityQueue.restype = None

def HeapSort(pq):
    """
    Sort the elements in the priority queue using heap sort algorithm.
    
    Args:
        pq (ctypes.c_void_p): Pointer to the priority queue structure.
        
    Returns:
        None
    """
    lib.HeapSort_PriorityQueue(pq)

# Display
lib.Display_PriorityQueue.argtypes = [ctypes.c_void_p]
lib.Display_PriorityQueue.restype = None

def Display(pq):
    """
    Display all elements in the priority queue to console.
    
    Args:
        pq (ctypes.c_void_p): Pointer to the priority queue structure.
        
    Returns:
        None
    """
    lib.Display_PriorityQueue(pq)