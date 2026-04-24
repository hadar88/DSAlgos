import os
import ctypes
from DataStructures_py.DisjointSetsItem import DisjointSetsItem

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# --- C Library Signatures ---
lib.Create_DisjointSets.argtypes = []
lib.Create_DisjointSets.restype = ctypes.c_void_p

lib.Destroy_DisjointSets.argtypes = [ctypes.c_void_p]
lib.Destroy_DisjointSets.restype = None

lib.MakeSet_DisjointSets.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.MakeSet_DisjointSets.restype = None

lib.FindSet_DisjointSets.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.FindSet_DisjointSets.restype = ctypes.c_void_p

lib.Union_DisjointSets.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
lib.Union_DisjointSets.restype = None

lib.Display_DisjointSets.argtypes = [ctypes.c_void_p]
lib.Display_DisjointSets.restype = None

class DisjointSets:
    """
    DisjointSets operations for disjoint sets.

    This module provides Python wrappers for C++ DisjointSets operations including
    creation, destruction, MakeSet, FindSet, Union, and Display operations.
    """
    def __init__(self, ptr: ctypes.c_void_p = None) -> None:
        if ptr:
            self.ptr = ptr
        else:
            self.ptr = lib.Create_DisjointSets()

    def __del__(self) -> None:
        """Automatically destroy the DisjointSets when the object is collected."""
        if hasattr(self, 'ptr') and self.ptr:
            lib.Destroy_DisjointSets(self.ptr)
            self.ptr = None

    def MakeSet(self, x: int) -> None:
        """Make a new set with the specified element."""
        lib.MakeSet_DisjointSets(self.ptr, x)

    def FindSet(self, x: int) -> DisjointSetsItem | None:
        """Find the set of the specified element (not owned)."""
        item_ptr = lib.FindSet_DisjointSets(self.ptr, x)
        return DisjointSetsItem(ptr=item_ptr, owned=False) if item_ptr else None

    def Union(self, x: int, y: int) -> None:
        """Union the sets of the specified elements."""
        lib.Union_DisjointSets(self.ptr, x, y)

    def Display(self) -> None:
        """Display the DisjointSets."""
        lib.Display_DisjointSets(self.ptr)