"""
PriorityQueue operations for heap-based priority queue data structures.

This module provides Python wrappers for C++ PriorityQueue operations including
creation, insertion, extraction, and heap operations. The priority queue is implemented
as a max-heap where the highest priority (maximum value) element is at the root.
"""
import os
import ctypes
from DataStructures_py.Utils import INT_MIN, C_INT_MIN

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# --- C Library Signatures ---
lib.Create_PriorityQueue.argtypes = []
lib.Create_PriorityQueue.restype = ctypes.c_void_p

lib.Destroy_PriorityQueue.argtypes = [ctypes.c_void_p]
lib.Destroy_PriorityQueue.restype = None

lib.IndexOf_PriorityQueue.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.IndexOf_PriorityQueue.restype = ctypes.c_int

lib.GetSize_PriorityQueue.argtypes = [ctypes.c_void_p]
lib.GetSize_PriorityQueue.restype = ctypes.c_int

lib.Maximum_PriorityQueue.argtypes = [ctypes.c_void_p]
lib.Maximum_PriorityQueue.restype = ctypes.c_int

lib.ExtractMax_PriorityQueue.argtypes = [ctypes.c_void_p]
lib.ExtractMax_PriorityQueue.restype = ctypes.c_int

lib.IncreaseKey_PriorityQueue.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
lib.IncreaseKey_PriorityQueue.restype = None

lib.Insert_PriorityQueue.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Insert_PriorityQueue.restype = None

lib.HeapSort_PriorityQueue.argtypes = [ctypes.c_void_p]
lib.HeapSort_PriorityQueue.restype = None

lib.Display_PriorityQueue.argtypes = [ctypes.c_void_p]
lib.Display_PriorityQueue.restype = None

class PriorityQueue:
    """A thin wrapper around a C++ PriorityQueue pointer."""
    def __init__(self, ptr: ctypes.c_void_p = None) -> None:
        if ptr:
            self.ptr = ptr
        else:
            self.ptr = lib.Create_PriorityQueue()

    def __del__(self) -> None:
        """Automatically destroy the priority queue when the object is collected."""
        if hasattr(self, 'ptr') and self.ptr:
            lib.Destroy_PriorityQueue(self.ptr)
            self.ptr = None

    def IndexOf(self, key: int) -> int:
        """Find the index of a given key in the priority queue."""
        return lib.IndexOf_PriorityQueue(self.ptr, key)

    def GetSize(self) -> int:
        """Get the number of elements in the priority queue."""
        return lib.GetSize_PriorityQueue(self.ptr)

    def Maximum(self) -> int:
        """Get the maximum element (highest priority) from the priority queue."""
        result = lib.Maximum_PriorityQueue(self.ptr)
        return INT_MIN if result == C_INT_MIN else result

    def ExtractMax(self) -> int:
        """Remove and return the maximum element from the priority queue."""
        result = lib.ExtractMax_PriorityQueue(self.ptr)
        return INT_MIN if result == C_INT_MIN else result

    def IncreaseKey(self, index: int, value: int) -> None:
        """Increase the priority of an element at a specific index."""
        lib.IncreaseKey_PriorityQueue(self.ptr, index, value)

    def Insert(self, value: int) -> None:
        """Insert a new element into the priority queue."""
        lib.Insert_PriorityQueue(self.ptr, value)

    def HeapSort(self) -> None:
        """Sort the elements in the priority queue using heap sort algorithm."""
        lib.HeapSort_PriorityQueue(self.ptr)

    def Display(self) -> None:
        """Display all elements in the priority queue to console."""
        lib.Display_PriorityQueue(self.ptr)