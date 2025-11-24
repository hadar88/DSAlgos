"""
Queue operations for FIFO (First In, First Out) data structures.

This module provides Python wrappers for C++ queue operations including
creation, enqueue, dequeue, and checking if the queue is empty. The queue follows
the FIFO principle where elements are added at the rear and removed from the front.
"""
import os
import ctypes

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# Create
lib.Create_queue.argtypes = []
lib.Create_queue.restype = ctypes.c_void_p

def Create():
    """
    Create a new empty queue.
    
    Returns:
        ctypes.c_void_p: A pointer to the queue structure.
    """
    return lib.Create_queue()

# Destroy
lib.Destroy_queue.argtypes = [ctypes.c_void_p]
lib.Destroy_queue.restype = None

def Destroy(queue):
    """
    Destroy the queue and free its memory.

    Args:
        queue (ctypes.c_void_p): Pointer to the queue structure.

    Returns:
        None
    """
    if queue:
        lib.Destroy_queue(queue)

# IsEmpty
lib.IsEmpty_queue.argtypes = [ctypes.c_void_p]
lib.IsEmpty_queue.restype = ctypes.c_bool

def IsEmpty(queue):
    """
    Check if the queue is empty.
    
    Args:
        queue (ctypes.c_void_p): Pointer to the queue structure.

    Returns:
        bool: True if the queue is empty (no elements), False otherwise.
    """
    return lib.IsEmpty_queue(queue)

# Enqueue
lib.Enqueue_queue.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Enqueue_queue.restype = None

def Enqueue(queue, value):
    """
    Add a new value to the rear of the queue.
    
    Args:
        queue (ctypes.c_void_p): Pointer to the queue structure.
        value (int): The integer value to add to the queue.
        
    Returns:
        None
    """
    lib.Enqueue_queue(queue, value)

# Dequeue
lib.Dequeue_queue.argtypes = [ctypes.c_void_p]
lib.Dequeue_queue.restype = ctypes.c_int

def Dequeue(queue):
    """
    Remove and return the front element from the queue.
    
    Args:
        queue (ctypes.c_void_p): Pointer to the queue structure.

    Returns:
        int: The value that was at the front of the queue.
    """
    return lib.Dequeue_queue(queue)

# Display
lib.Display_queue.argtypes = [ctypes.c_void_p]
lib.Display_queue.restype = None

def Display(queue):
    """
    Display all elements in the queue to console.
    
    Args:
        queue (ctypes.c_void_p): Pointer to the queue structure.

    Returns:
        None
    """
    lib.Display_queue(queue)