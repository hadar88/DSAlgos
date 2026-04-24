from __future__ import annotations

import os
import ctypes
from DataStructures_py.Utils import INT_MIN, C_INT_MIN

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# --- C Library Signatures ---
lib.Create_SkipListNode.argtypes = [ctypes.c_int, ctypes.c_int]
lib.Create_SkipListNode.restype = ctypes.c_void_p

lib.Destroy_SkipListNode.argtypes = [ctypes.c_void_p]
lib.Destroy_SkipListNode.restype = None

lib.GetData_SkipListNode.argtypes = [ctypes.c_void_p]
lib.GetData_SkipListNode.restype = ctypes.c_int

lib.GetHeight_SkipListNode.argtypes = [ctypes.c_void_p]
lib.GetHeight_SkipListNode.restype = ctypes.c_int

lib.GetNext_SkipListNode.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.GetNext_SkipListNode.restype = ctypes.c_void_p

lib.GetPrev_SkipListNode.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.GetPrev_SkipListNode.restype = ctypes.c_void_p

lib.SetData_SkipListNode.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.SetData_SkipListNode.restype = None

lib.SetHeight_SkipListNode.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.SetHeight_SkipListNode.restype = None

lib.SetNext_SkipListNode.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
lib.SetNext_SkipListNode.restype = None

lib.SetPrev_SkipListNode.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
lib.SetPrev_SkipListNode.restype = None

class SkipListNode:
    """
    SkipListNode operations for skip list data structures.

    This module provides Python wrappers for C++ SkipListNode operations including
    creation, data access, and navigation through multiple levels. Skip list nodes
    support probabilistic data structure operations with multiple forward/backward pointers.
    """
    def __init__(self, value: int | None = None, height: int | None = None, ptr: ctypes.c_void_p = None, owned: bool = True) -> None:
        self.owned = owned
        if ptr:
            self.ptr = ptr
        else:
            if value is None or height is None:
                raise ValueError("value and height must be provided when ptr is not supplied")
            self.ptr = lib.Create_SkipListNode(value, height)

    def __del__(self) -> None:
        """Automatically destroy the skip list node when the object is collected."""
        if self.owned and hasattr(self, 'ptr') and self.ptr:
            lib.Destroy_SkipListNode(self.ptr)
            self.ptr = None

    def GetData(self) -> int | float:
        """Get the data value stored in this node."""
        data = lib.GetData_SkipListNode(self.ptr)
        return INT_MIN if data == C_INT_MIN else data

    def GetHeight(self) -> int:
        """Get the height of this node."""
        return lib.GetHeight_SkipListNode(self.ptr)

    def GetNext(self, level: int) -> SkipListNode | None:
        """Get the next node at a specific level (not owned)."""
        node_ptr = lib.GetNext_SkipListNode(self.ptr, level)
        return SkipListNode(ptr=node_ptr, owned=False) if node_ptr else None

    def GetPrev(self, level: int) -> SkipListNode | None:
        """Get the previous node at a specific level (not owned)."""
        node_ptr = lib.GetPrev_SkipListNode(self.ptr, level)
        return SkipListNode(ptr=node_ptr, owned=False) if node_ptr else None

    def SetData(self, value: int) -> None:
        """Set the data value of this node."""
        lib.SetData_SkipListNode(self.ptr, value)

    def SetHeight(self, height: int) -> None:
        """Set the height of this node."""
        lib.SetHeight_SkipListNode(self.ptr, height)

    def SetNext(self, level: int, next_node: SkipListNode | None) -> None:
        """Set the next node pointer at a specific level."""
        ptr = next_node.ptr if next_node else None
        lib.SetNext_SkipListNode(self.ptr, level, ptr)

    def SetPrev(self, level: int, prev_node: SkipListNode | None) -> None:
        """Set the previous node pointer at a specific level."""
        ptr = prev_node.ptr if prev_node else None
        lib.SetPrev_SkipListNode(self.ptr, level, ptr)