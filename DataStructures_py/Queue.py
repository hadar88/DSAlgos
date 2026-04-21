"""
Queue operations for FIFO (First In, First Out) data structures.

This module provides Python wrappers for C++ queue operations.
All operations are encapsulated within the Queue class.
"""
import os
import ctypes
from DataStructures_py.Utils import INT_MIN, C_INT_MIN

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# --- C Library Signatures ---
lib.Create_queue.argtypes = []
lib.Create_queue.restype = ctypes.c_void_p

lib.Destroy_queue.argtypes = [ctypes.c_void_p]
lib.Destroy_queue.restype = None

lib.IsEmpty_queue.argtypes = [ctypes.c_void_p]
lib.IsEmpty_queue.restype = ctypes.c_bool

lib.Enqueue_queue.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Enqueue_queue.restype = None

lib.Dequeue_queue.argtypes = [ctypes.c_void_p]
lib.Dequeue_queue.restype = ctypes.c_int

lib.Display_queue.argtypes = [ctypes.c_void_p]
lib.Display_queue.restype = None

class Queue:
    """A thin wrapper around a C++ queue pointer."""
    def __init__(self, ptr: ctypes.c_void_p = None) -> None:
        if ptr is not None:
            self.ptr = ptr
        else:
            self.ptr = lib.Create_queue()

    def __del__(self) -> None:
        """Automatically destroy the queue when the object is collected."""
        if hasattr(self, 'ptr') and self.ptr:
            lib.Destroy_queue(self.ptr)
            self.ptr = None

    def IsEmpty(self) -> bool:
        """Check if the queue is empty."""
        return lib.IsEmpty_queue(self.ptr)

    def Enqueue(self, value: int) -> None:
        """Add a value to the rear of the queue."""
        lib.Enqueue_queue(self.ptr, value)

    def Dequeue(self) -> int:
        """Remove and return the front element from the queue."""
        result = lib.Dequeue_queue(self.ptr)
        return INT_MIN if result == C_INT_MIN else result

    def Display(self) -> None:
        """Display all elements in the queue to console."""
        lib.Display_queue(self.ptr)