import os
import ctypes
from ..Utils import INT_MAX, INT_MIN, C_INT_MAX, C_INT_MIN
from .TreeNode import TreeNode

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "dstructures.so"))

# --- C Library Signatures ---
lib.Create_AVLTree.argtypes = []
lib.Create_AVLTree.restype = ctypes.c_void_p

lib.Destroy_AVLTree.argtypes = [ctypes.c_void_p]
lib.Destroy_AVLTree.restype = None

lib.IsEmpty_AVLTree.argtypes = [ctypes.c_void_p]
lib.IsEmpty_AVLTree.restype = ctypes.c_bool

lib.Size_AVLTree.argtypes = [ctypes.c_void_p]
lib.Size_AVLTree.restype = ctypes.c_int

lib.GetRoot_AVLTree.argtypes = [ctypes.c_void_p]
lib.GetRoot_AVLTree.restype = ctypes.c_void_p

lib.Exists_AVLTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Exists_AVLTree.restype = ctypes.c_bool

lib.Search_AVLTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Search_AVLTree.restype = ctypes.c_void_p

lib.Minimum_AVLTree.argtypes = [ctypes.c_void_p]
lib.Minimum_AVLTree.restype = ctypes.c_int

lib.Maximum_AVLTree.argtypes = [ctypes.c_void_p]
lib.Maximum_AVLTree.restype = ctypes.c_int

lib.Successor_AVLTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Successor_AVLTree.restype = ctypes.c_void_p

lib.Insert_AVLTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Insert_AVLTree.restype = None

lib.Delete_AVLTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Delete_AVLTree.restype = None

lib.Depth_AVLTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Depth_AVLTree.restype = ctypes.c_int

lib.Height_AVLTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Height_AVLTree.restype = ctypes.c_int

lib.InOrder_AVLTree.argtypes = [ctypes.c_void_p]
lib.InOrder_AVLTree.restype = None

lib.PreOrder_AVLTree.argtypes = [ctypes.c_void_p]
lib.PreOrder_AVLTree.restype = None

lib.PostOrder_AVLTree.argtypes = [ctypes.c_void_p]
lib.PostOrder_AVLTree.restype = None


class AVLTree:
    """
    AVL Tree operations for self-balancing binary search trees.

    This module provides Python wrappers for C++ AVL Tree operations including
    creation, insertion, deletion, searching, and traversal. AVL trees automatically
    maintain balance through rotations, ensuring O(log n) performance for all operations.

    This module works in conjunction with the TreeNode module.
    """

    def __init__(self, ptr: ctypes.c_void_p = None) -> None:
        if ptr:
            self.ptr = ptr
        else:
            self.ptr = lib.Create_AVLTree()

    def __del__(self) -> None:
        """Automatically destroy the AVL tree when the object is collected."""
        if hasattr(self, "ptr") and self.ptr:
            lib.Destroy_AVLTree(self.ptr)
            self.ptr = None

    def IsEmpty(self) -> bool:
        """Check if the AVL tree is empty."""
        return lib.IsEmpty_AVLTree(self.ptr)

    def Size(self) -> int:
        """Get the number of nodes in the AVL tree."""
        return lib.Size_AVLTree(self.ptr)

    def GetRoot(self) -> TreeNode | None:
        """Get the root node of the AVL tree (not owned)."""
        root_ptr = lib.GetRoot_AVLTree(self.ptr)
        return TreeNode(ptr=root_ptr, owned=False) if root_ptr else None

    def Exists(self, key: int) -> bool:
        """Check if a key exists in the AVL tree."""
        return lib.Exists_AVLTree(self.ptr, key)

    def Search(self, key: int) -> TreeNode | None:
        """Search for a key in the AVL tree and return the node (not owned)."""
        node_ptr = lib.Search_AVLTree(self.ptr, key)
        return TreeNode(ptr=node_ptr, owned=False) if node_ptr else None

    def Minimum(self) -> int | float:
        """Find the minimum value in the AVL tree."""
        result = lib.Minimum_AVLTree(self.ptr)
        return INT_MIN if result == C_INT_MIN else result

    def Maximum(self) -> int | float:
        """Find the maximum value in the AVL tree."""
        result = lib.Maximum_AVLTree(self.ptr)
        return INT_MAX if result == C_INT_MAX else result

    def Successor(self, key: int) -> TreeNode | None:
        """Find the successor of a given key in the AVL tree (not owned)."""
        node_ptr = lib.Successor_AVLTree(self.ptr, key)
        return TreeNode(ptr=node_ptr, owned=False) if node_ptr else None

    def Insert(self, key: int) -> None:
        """Insert a new key into the AVL tree with automatic balancing."""
        lib.Insert_AVLTree(self.ptr, key)

    def Delete(self, key: int) -> None:
        """Delete a key from the AVL tree with automatic rebalancing."""
        lib.Delete_AVLTree(self.ptr, key)

    def Depth(self, key: int) -> int:
        """Get the depth of a specific key in the AVL tree."""
        return lib.Depth_AVLTree(self.ptr, key)

    def Height(self, key: int) -> int:
        """Get the height of a specific node in the AVL tree."""
        return lib.Height_AVLTree(self.ptr, key)

    def InOrder(self) -> None:
        """Perform inorder traversal of the AVL tree."""
        lib.InOrder_AVLTree(self.ptr)

    def PreOrder(self) -> None:
        """Perform preorder traversal of the AVL tree."""
        lib.PreOrder_AVLTree(self.ptr)

    def PostOrder(self) -> None:
        """Perform postorder traversal of the AVL tree."""
        lib.PostOrder_AVLTree(self.ptr)
