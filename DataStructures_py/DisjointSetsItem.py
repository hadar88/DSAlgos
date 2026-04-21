"""
SetItem operations for disjoint sets.

This module provides Python wrappers for C++ SetItem operations including
creation, data access, and pointer manipulation for SetItems.
"""
from __future__ import annotations

import os
import ctypes

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# --- C Library Signatures ---
lib.Create_SetItem.argtypes = [ctypes.c_int]
lib.Create_SetItem.restype = ctypes.c_void_p

lib.Destroy_SetItem.argtypes = [ctypes.c_void_p]
lib.Destroy_SetItem.restype = None

lib.GetData_SetItem.argtypes = [ctypes.c_void_p]
lib.GetData_SetItem.restype = ctypes.c_int

lib.GetRank_SetItem.argtypes = [ctypes.c_void_p]
lib.GetRank_SetItem.restype = ctypes.c_int

lib.GetParent_SetItem.argtypes = [ctypes.c_void_p]
lib.GetParent_SetItem.restype = ctypes.c_void_p

lib.SetRank_SetItem.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.SetRank_SetItem.restype = None

lib.SetParent_SetItem.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.SetParent_SetItem.restype = None

class DisjointSetsItem:
    """A thin wrapper around a C++ SetItem pointer."""
    def __init__(self, value: int = None, ptr : ctypes.c_void_p = None, owned: bool = True) -> None:
        self.owned = owned
        if ptr:
            self.ptr = ptr
        else:
            self.ptr = lib.Create_SetItem(value)

    def __del__(self) -> None:
        """Automatically destroy the SetItem when the object is collected."""
        if self.owned and hasattr(self, 'ptr') and self.ptr:
            lib.Destroy_SetItem(self.ptr)
            self.ptr = None

    def GetData(self) -> int:
        """Get the data of the SetItem."""
        return lib.GetData_SetItem(self.ptr)

    def GetRank(self) -> int:
        """Get the rank of the SetItem."""
        return lib.GetRank_SetItem(self.ptr)

    def GetParent(self) -> DisjointSetsItem:
        """Get the parent of the SetItem (not owned)."""
        parent_ptr = lib.GetParent_SetItem(self.ptr)
        return DisjointSetsItem(ptr=parent_ptr, owned=False) if parent_ptr else None

    def SetRank(self, rank: int) -> None:
        """Set the rank of the SetItem."""
        lib.SetRank_SetItem(self.ptr, rank)

    def SetParent(self, parent: DisjointSetsItem) -> None:
        """Set the parent of the SetItem."""
        parent_ptr = parent.ptr if parent else None
        lib.SetParent_SetItem(self.ptr, parent_ptr)