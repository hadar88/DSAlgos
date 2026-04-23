from __future__ import annotations

import os
import ctypes
from DataStructures_py.Utils import INT_MIN, C_INT_MIN

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# --- C Library Signatures ---
lib.Create_node.argtypes = [ctypes.c_int]
lib.Create_node.restype = ctypes.c_void_p

lib.Destroy_node.argtypes = [ctypes.c_void_p]
lib.Destroy_node.restype = None

lib.GetData_node.argtypes = [ctypes.c_void_p]
lib.GetData_node.restype = ctypes.c_int

lib.GetNext_node.argtypes = [ctypes.c_void_p]
lib.GetNext_node.restype = ctypes.c_void_p

lib.SetData_node.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.SetData_node.restype = None

lib.SetNext_node.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.SetNext_node.restype = None

class Node:
    """
    Node operations for linked data structures.

    This module provides Python wrappers for C++ node operations.
    All operations are encapsulated within the Node class.
    """
    def __init__(self, value: int | None = None, ptr: ctypes.c_void_p = None, owned: bool = True) -> None:
        self.owned = owned
        if ptr is not None:
            self.ptr = ptr
        else:
            if value is None:
                raise ValueError("value must be provided when ptr is not supplied")
            self.ptr = lib.Create_node(value)

    def __del__(self) -> None:
        """Automatically destroy the node only if it is owned by this object."""
        if self.owned and hasattr(self, 'ptr') and self.ptr:
            lib.Destroy_node(self.ptr)
            self.ptr = None

    def GetData(self) -> int:
        """Get the data value stored in this node."""
        val = lib.GetData_node(self.ptr)
        return INT_MIN if val == C_INT_MIN else val

    def GetNext(self) -> Node:
        """Get the next node as a Node instance (not owned)."""
        next_ptr = lib.GetNext_node(self.ptr)
        return Node(ptr=next_ptr, owned=False) if next_ptr else None

    def SetData(self, value: int) -> None:
        """Set the data value of this node."""
        lib.SetData_node(self.ptr, value)

    def SetNext(self, next_node: Node | None) -> None:
        """Set the next node pointer."""
        ptr = next_node.ptr if next_node else None
        lib.SetNext_node(self.ptr, ptr)