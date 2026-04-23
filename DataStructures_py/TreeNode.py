from __future__ import annotations

import os
import ctypes
from DataStructures_py.Utils import INT_MIN, C_INT_MIN

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# --- C Library Signatures ---
lib.Create_treenode.argtypes = [ctypes.c_int]
lib.Create_treenode.restype = ctypes.c_void_p

lib.Destroy_treenode.argtypes = [ctypes.c_void_p]
lib.Destroy_treenode.restype = None

lib.GetData_treenode.argtypes = [ctypes.c_void_p]
lib.GetData_treenode.restype = ctypes.c_int

lib.GetRight_treenode.argtypes = [ctypes.c_void_p]
lib.GetRight_treenode.restype = ctypes.c_void_p

lib.GetLeft_treenode.argtypes = [ctypes.c_void_p]
lib.GetLeft_treenode.restype = ctypes.c_void_p

lib.GetParent_treenode.argtypes = [ctypes.c_void_p]
lib.GetParent_treenode.restype = ctypes.c_void_p

lib.SetData_treenode.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.SetData_treenode.restype = None

lib.SetRight_treenode.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.SetRight_treenode.restype = None

lib.SetLeft_treenode.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.SetLeft_treenode.restype = None

lib.SetParent_treenode.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.SetParent_treenode.restype = None

class TreeNode:
    """
    TreeNode operations for tree data structures.

    This module provides Python wrappers for C++ tree node operations.
    All operations are encapsulated within the TreeNode class.
    """
    def __init__(self, value: int | None = None, ptr: ctypes.c_void_p = None, owned: bool = True) -> None:
        self.owned = owned
        if ptr is not None:
            self.ptr = ptr
        else:
            if value is None:
                raise ValueError("value must be provided when ptr is not supplied")
            self.ptr = lib.Create_treenode(value)

    def __del__(self) -> None:
        """Automatically destroy the node only if it is owned by this object."""
        if self.owned and hasattr(self, 'ptr') and self.ptr:
            lib.Destroy_treenode(self.ptr)
            self.ptr = None

    def GetData(self) -> int:
        """Get the data value stored in this node."""
        val = lib.GetData_treenode(self.ptr)
        return INT_MIN if val == C_INT_MIN else val

    def GetLeft(self) -> TreeNode | None:
        """Get the left child as a TreeNode instance (not owned)."""
        ptr = lib.GetLeft_treenode(self.ptr)
        return TreeNode(ptr=ptr, owned=False) if ptr else None

    def GetRight(self) -> TreeNode | None:
        """Get the right child as a TreeNode instance (not owned)."""
        ptr = lib.GetRight_treenode(self.ptr)
        return TreeNode(ptr=ptr, owned=False) if ptr else None

    def GetParent(self) -> TreeNode | None:
        """Get the parent as a TreeNode instance (not owned)."""
        ptr = lib.GetParent_treenode(self.ptr)
        return TreeNode(ptr=ptr, owned=False) if ptr else None

    def SetData(self, value: int) -> None:
        """Set the data value of this node."""
        lib.SetData_treenode(self.ptr, value)

    def SetLeft(self, left_node: TreeNode) -> None:
        """Set the left child node."""
        ptr = left_node.ptr if left_node else None
        lib.SetLeft_treenode(self.ptr, ptr)

    def SetRight(self, right_node: TreeNode) -> None:
        """Set the right child node."""
        ptr = right_node.ptr if right_node else None
        lib.SetRight_treenode(self.ptr, ptr)

    def SetParent(self, parent_node: TreeNode) -> None:
        """Set the parent node."""
        ptr = parent_node.ptr if parent_node else None
        lib.SetParent_treenode(self.ptr, ptr)