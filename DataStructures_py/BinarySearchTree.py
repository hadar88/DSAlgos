import os
import ctypes
from DataStructures_py.Utils import INT_MAX, INT_MIN, C_INT_MAX, C_INT_MIN
from DataStructures_py.TreeNode import TreeNode

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# --- C Library Signatures ---
lib.Create_BinarySearchTree.argtypes = []
lib.Create_BinarySearchTree.restype = ctypes.c_void_p

lib.Destroy_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.Destroy_BinarySearchTree.restype = None

lib.IsEmpty_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.IsEmpty_BinarySearchTree.restype = ctypes.c_bool

lib.Size_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.Size_BinarySearchTree.restype = ctypes.c_int

lib.GetRoot_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.GetRoot_BinarySearchTree.restype = ctypes.c_void_p

lib.Exists_BinarySearchTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Exists_BinarySearchTree.restype = ctypes.c_bool

lib.Search_BinarySearchTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Search_BinarySearchTree.restype = ctypes.c_void_p

lib.Minimum_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.Minimum_BinarySearchTree.restype = ctypes.c_int

lib.Maximum_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.Maximum_BinarySearchTree.restype = ctypes.c_int

lib.Successor_BinarySearchTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Successor_BinarySearchTree.restype = ctypes.c_void_p

lib.Insert_BinarySearchTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Insert_BinarySearchTree.restype = None

lib.Delete_BinarySearchTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Delete_BinarySearchTree.restype = None

lib.Depth_BinarySearchTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Depth_BinarySearchTree.restype = ctypes.c_int

lib.Height_BinarySearchTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Height_BinarySearchTree.restype = ctypes.c_int

lib.InOrder_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.InOrder_BinarySearchTree.restype = None

lib.PreOrder_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.PreOrder_BinarySearchTree.restype = None

lib.PostOrder_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.PostOrder_BinarySearchTree.restype = None

class BinarySearchTree:
    """
    Binary Search Tree operations for ordered tree data structures.

    This module provides Python wrappers for C++ Binary Search Tree operations.
    All operations are encapsulated within the BinarySearchTree class.
    """
    def __init__(self, ptr: ctypes.c_void_p = None) -> None:
        if ptr is not None:
            self.ptr = ptr
        else:
            self.ptr = lib.Create_BinarySearchTree()

    def __del__(self) -> None:
        """Automatically destroy the tree when the object is collected."""
        if hasattr(self, 'ptr') and self.ptr:
            lib.Destroy_BinarySearchTree(self.ptr)
            self.ptr = None

    def IsEmpty(self) -> bool:
        """Check if the tree is empty."""
        return lib.IsEmpty_BinarySearchTree(self.ptr)

    def Size(self) -> int:
        """Get the number of nodes in the tree."""
        return lib.Size_BinarySearchTree(self.ptr)

    def GetRoot(self) -> TreeNode:
        """Get the root node as a TreeNode instance (not owned)."""
        ptr = lib.GetRoot_BinarySearchTree(self.ptr)
        return TreeNode(ptr=ptr, owned=False) if ptr else None

    def Exists(self, key: int) -> bool:
        """Check if a key exists in the tree."""
        return lib.Exists_BinarySearchTree(self.ptr, key)

    def Search(self, key: int) -> TreeNode | None:
        """Search for a key and return the node as a TreeNode instance (not owned)."""
        ptr = lib.Search_BinarySearchTree(self.ptr, key)
        return TreeNode(ptr=ptr, owned=False) if ptr else None

    def Minimum(self) -> int:
        """Find the minimum value in the tree."""
        result = lib.Minimum_BinarySearchTree(self.ptr)
        return INT_MIN if result == C_INT_MIN else result

    def Maximum(self) -> int:
        """Find the maximum value in the tree."""
        result = lib.Maximum_BinarySearchTree(self.ptr)
        return INT_MAX if result == C_INT_MAX else result

    def Successor(self, key: int) -> TreeNode | None:
        """Find the successor of a key and return as a TreeNode instance (not owned)."""
        ptr = lib.Successor_BinarySearchTree(self.ptr, key)
        return TreeNode(ptr=ptr, owned=False) if ptr else None

    def Insert(self, key: int) -> None:
        """Insert a new key into the tree."""
        lib.Insert_BinarySearchTree(self.ptr, key)

    def Delete(self, key: int) -> None:
        """Delete a key from the tree."""
        lib.Delete_BinarySearchTree(self.ptr, key)

    def Depth(self, key: int) -> int:
        """Get the depth of a specific key."""
        return lib.Depth_BinarySearchTree(self.ptr, key)

    def Height(self, key: int) -> int:
        """Get the height of a specific node."""
        return lib.Height_BinarySearchTree(self.ptr, key)

    def InOrder(self) -> None:
        """Perform inorder traversal (displays to console)."""
        lib.InOrder_BinarySearchTree(self.ptr)

    def PreOrder(self) -> None:
        """Perform preorder traversal (displays to console)."""
        lib.PreOrder_BinarySearchTree(self.ptr)

    def PostOrder(self) -> None:
        """Perform postorder traversal (displays to console)."""
        lib.PostOrder_BinarySearchTree(self.ptr)
