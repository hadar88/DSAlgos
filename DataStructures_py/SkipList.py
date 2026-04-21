"""
SkipList operations for probabilistic data structures.

This module provides Python wrappers for C++ SkipList operations including
creation, insertion, deletion, and searching. Skip lists provide probabilistic
balancing with expected O(log n) performance for search, insert, and delete operations.

This module works in conjunction with the SkipListNode module.
"""
import os
import ctypes
from DataStructures_py.SkipListNode import SkipListNode

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# --- C Library Signatures ---
lib.Create_SkipList.argtypes = None
lib.Create_SkipList.restype = ctypes.c_void_p

lib.Destroy_SkipList.argtypes = [ctypes.c_void_p]
lib.Destroy_SkipList.restype = None

lib.IsEmpty_SkipList.argtypes = [ctypes.c_void_p]
lib.IsEmpty_SkipList.restype = ctypes.c_bool

lib.GetHead_SkipList.argtypes = [ctypes.c_void_p]
lib.GetHead_SkipList.restype = ctypes.c_void_p

lib.GetHeight_SkipList.argtypes = [ctypes.c_void_p]
lib.GetHeight_SkipList.restype = ctypes.c_int

lib.Search_SkipList.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Search_SkipList.restype = ctypes.c_void_p

lib.Insert_SkipList.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Insert_SkipList.restype = None

lib.Delete_SkipList.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Delete_SkipList.restype = None

lib.Display_SkipList.argtypes = [ctypes.c_void_p]
lib.Display_SkipList.restype = None

class SkipList:
    """A thin wrapper around a C++ SkipList pointer."""
    def __init__(self, ptr: ctypes.c_void_p = None, owned: bool = True) -> None:
        self.owned = owned
        if ptr:
            self.ptr = ptr
        else:
            self.ptr = lib.Create_SkipList()

    def __del__(self) -> None:
        """Automatically destroy the skip list when the object is collected."""
        if self.owned and hasattr(self, 'ptr') and self.ptr:
            lib.Destroy_SkipList(self.ptr)
            self.ptr = None

    def IsEmpty(self) -> bool:
        """Check if the skip list is empty."""
        return lib.IsEmpty_SkipList(self.ptr)

    def GetHead(self) -> SkipListNode | None:
        """Get the head node of the skip list (not owned)."""
        node_ptr = lib.GetHead_SkipList(self.ptr)
        return SkipListNode(ptr=node_ptr, owned=False) if node_ptr else None

    def GetHeight(self) -> int:
        """Get the current height of the skip list."""
        return lib.GetHeight_SkipList(self.ptr)

    def Search(self, key: int) -> SkipListNode | None:
        """Search for a key in the skip list and return the node (not owned)."""
        node_ptr = lib.Search_SkipList(self.ptr, key)
        return SkipListNode(ptr=node_ptr, owned=False) if node_ptr else None

    def Insert(self, key: int) -> None:
        """Insert a new key into the skip list with probabilistic height assignment."""
        lib.Insert_SkipList(self.ptr, key)

    def Delete(self, key: int) -> None:
        """Delete a key from the skip list."""
        lib.Delete_SkipList(self.ptr, key)

    def Display(self) -> None:
        """Display all elements in the skip list to console."""
        lib.Display_SkipList(self.ptr)