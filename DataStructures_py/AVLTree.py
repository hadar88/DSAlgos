"""
AVL Tree operations for self-balancing binary search trees.

This module provides Python wrappers for C++ AVL Tree operations including
creation, insertion, deletion, searching, and traversal. AVL trees automatically
maintain balance through rotations, ensuring O(log n) performance for all operations.

This module works in conjunction with the TreeNode module.
"""
import os
import ctypes

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# Create
lib.Create_AVLTree.argtypes = []
lib.Create_AVLTree.restype = ctypes.c_void_p

def Create():
    """
    Create a new empty AVL tree.
    
    Returns:
        ctypes.c_void_p: A pointer to the AVL tree structure.
    """
    return lib.Create_AVLTree()

# Destroy
lib.Destroy_AVLTree.argtypes = [ctypes.c_void_p]
lib.Destroy_AVLTree.restype = None

def Destroy(tree):
    """
    Destroy the AVL tree and free its memory.

    Args:
        tree (ctypes.c_void_p): Pointer to the AVL tree structure.

    Returns:
        None
    """
    if tree:
        lib.Destroy_AVLTree(tree)

# IsEmpty
lib.IsEmpty_AVLTree.argtypes = [ctypes.c_void_p]
lib.IsEmpty_AVLTree.restype = ctypes.c_bool

def IsEmpty(tree):
    """
    Check if the AVL tree is empty.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the AVL tree structure.

    Returns:
        bool: True if the tree is empty (no nodes), False otherwise.
    """
    return lib.IsEmpty_AVLTree(tree)

# GetRoot
lib.GetRoot_AVLTree.argtypes = [ctypes.c_void_p]
lib.GetRoot_AVLTree.restype = ctypes.c_void_p

def GetRoot(tree):
    """
    Get the root node of the AVL tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the AVL tree structure.

    Returns:
        ctypes.c_void_p: Pointer to the root TreeNode, or None if tree is empty.
    """
    return lib.GetRoot_AVLTree(tree)

# Exists
lib.Exists_AVLTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Exists_AVLTree.restype = ctypes.c_bool

def Exists(tree, key):
    """
    Check if a key exists in the AVL tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the AVL tree structure.
        key (int): The value to search for.
        
    Returns:
        bool: True if the key exists in the tree, False otherwise.
    """
    return lib.Exists_AVLTree(tree, key)

# Search
lib.Search_AVLTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Search_AVLTree.restype = ctypes.c_void_p

def Search(tree, key):
    """
    Search for a key in the AVL tree and return the node.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the AVL tree structure.
        key (int): The value to search for.
        
    Returns:
        ctypes.c_void_p: Pointer to the TreeNode containing the key, or None if not found.
    """
    return lib.Search_AVLTree(tree, key)

# Minimum
lib.Minimum_AVLTree.argtypes = [ctypes.c_void_p]
lib.Minimum_AVLTree.restype = ctypes.c_void_p

def Minimum(tree):
    """
    Find the node with minimum value in the AVL tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the AVL tree structure.

    Returns:
        ctypes.c_void_p: Pointer to the TreeNode with the smallest value.
    """
    return lib.Minimum_AVLTree(tree)

# Maximum
lib.Maximum_AVLTree.argtypes = [ctypes.c_void_p]
lib.Maximum_AVLTree.restype = ctypes.c_void_p

def Maximum(tree):
    """
    Find the node with maximum value in the AVL tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the AVL tree structure.

    Returns:
        ctypes.c_void_p: Pointer to the TreeNode with the largest value.
    """
    return lib.Maximum_AVLTree(tree)

# Successor
lib.Successor_AVLTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Successor_AVLTree.restype = ctypes.c_void_p

def Successor(tree, key):
    """
    Find the successor of a given key in the AVL tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the AVL tree structure.
        key (int): The value whose successor to find.
        
    Returns:
        ctypes.c_void_p: Pointer to the TreeNode containing the successor value, or None if no successor.
    """
    return lib.Successor_AVLTree(tree, key)

# Insert
lib.Insert_AVLTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Insert_AVLTree.restype = None

def Insert(tree, key):
    """
    Insert a new key into the AVL tree with automatic balancing.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the AVL tree structure.
        key (int): The value to insert.
        
    Returns:
        None
    """
    lib.Insert_AVLTree(tree, key)

# Delete
lib.Delete_AVLTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Delete_AVLTree.restype = None

def Delete(tree, key):
    """
    Delete a key from the AVL tree with automatic rebalancing.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the AVL tree structure.
        key (int): The value to delete.
        
    Returns:
        None
    """
    lib.Delete_AVLTree(tree, key)

# Depth
lib.Depth_AVLTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Depth_AVLTree.restype = ctypes.c_int

def Depth(tree, key):
    """
    Get the depth of a specific key in the AVL tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the AVL tree structure.
        key (int): The value whose depth to find.
        
    Returns:
        int: The depth of the node (distance from root), or -1 if key not found.
    """
    return lib.Depth_AVLTree(tree, key)

# Height
lib.Height_AVLTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Height_AVLTree.restype = ctypes.c_int

def Height(tree, key):
    """
    Get the height of a specific node in the AVL tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the AVL tree structure.
        key (int): The value whose height to find.
        
    Returns:
        int: The height of the node (distance to furthest leaf), or -1 if key not found.
    """
    return lib.Height_AVLTree(tree, key)

# InOrder
lib.InOrder_AVLTree.argtypes = [ctypes.c_void_p]
lib.InOrder_AVLTree.restype = None

def InOrder(tree):
    """
    Perform inorder traversal of the AVL tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the AVL tree structure.

    Returns:
        None
    """
    lib.InOrder_AVLTree(tree)

# PreOrder
lib.PreOrder_AVLTree.argtypes = [ctypes.c_void_p]
lib.PreOrder_AVLTree.restype = None

def PreOrder(tree):
    """
    Perform preorder traversal of the AVL tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the AVL tree structure.

    Returns:
        None
    """
    lib.PreOrder_AVLTree(tree)

# PostOrder
lib.PostOrder_AVLTree.argtypes = [ctypes.c_void_p]
lib.PostOrder_AVLTree.restype = None

def PostOrder(tree):
    """
    Perform postorder traversal of the AVL tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the AVL tree structure.

    Returns:
        None
    """
    lib.PostOrder_AVLTree(tree)