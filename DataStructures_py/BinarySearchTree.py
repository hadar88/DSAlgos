"""
Binary Search Tree operations for ordered tree data structures.

This module provides Python wrappers for C++ Binary Search Tree operations including
creation, insertion, deletion, searching, and traversal. BST maintains the property
that left subtree values are less than the node value, and right subtree values are greater.

Note:
    This module works in conjunction with the TreeNode module.
"""
import os
import ctypes

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# Create
lib.Create_BinarySearchTree.argtypes = []
lib.Create_BinarySearchTree.restype = ctypes.c_void_p

def Create():
    """
    Create a new empty binary search tree.
    
    Returns:
        ctypes.c_void_p: A pointer to the BST structure.
    """
    return lib.Create_BinarySearchTree()

# Destroy
lib.Destroy_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.Destroy_BinarySearchTree.restype = None

def Destroy(tree):
    """
    Destroy the binary search tree and free its memory.

    Args:
        tree (ctypes.c_void_p): Pointer to the BST structure.

    Returns:
        None
    """
    if tree:
        lib.Destroy_BinarySearchTree(tree)

# IsEmpty
lib.IsEmpty_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.IsEmpty_BinarySearchTree.restype = ctypes.c_bool

def IsEmpty(tree):
    """
    Create a new empty binary search tree.
    
    Returns:
        ctypes.c_void_p: A pointer to the BST structure.

    Note:
        The created BST is initially empty with no root node.
        Use Insert() to add elements to the tree.
    """
    return lib.IsEmpty_BinarySearchTree(tree)

# GetRoot
lib.GetRoot_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.GetRoot_BinarySearchTree.restype = ctypes.c_void_p

def GetRoot(tree):
    """
    Get the root node of the binary search tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the BST structure.

    Returns:
        ctypes.c_void_p: Pointer to the root TreeNode, or None if tree is empty.
    """
    return lib.GetRoot_BinarySearchTree(tree)

# Exists
lib.Exists_BinarySearchTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Exists_BinarySearchTree.restype = ctypes.c_bool

def Exists(tree, key):
    """
    Check if a key exists in the binary search tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the BST structure.
        key (int): The value to search for.
        
    Returns:
        bool: True if the key exists in the tree, False otherwise.
    """
    return lib.Exists_BinarySearchTree(tree, key)

# Search
lib.Search_BinarySearchTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Search_BinarySearchTree.restype = ctypes.c_void_p

def Search(tree, key):
    """
    Search for a key in the binary search tree and return the node.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the BST structure.
        key (int): The value to search for.
        
    Returns:
        ctypes.c_void_p: Pointer to the TreeNode containing the key, or None if not found.
    """
    return lib.Search_BinarySearchTree(tree, key)

# Minimum
lib.Minimum_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.Minimum_BinarySearchTree.restype = ctypes.c_int

def Minimum(tree):
    """
    Find the minimum value in the binary search tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the BST structure.

    Returns:
        int: The smallest value in the tree.
    """
    return lib.Minimum_BinarySearchTree(tree)

# Maximum
lib.Maximum_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.Maximum_BinarySearchTree.restype = ctypes.c_int

def Maximum(tree):
    """
    Find the maximum value in the binary search tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the BST structure.

    Returns:
        int: The largest value in the tree.
    """
    return lib.Maximum_BinarySearchTree(tree)

# Successor
lib.Successor_BinarySearchTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Successor_BinarySearchTree.restype = ctypes.c_void_p

def Successor(tree, key):
    """
    Find the successor of a given key in the binary search tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the BST structure.
        key (int): The value whose successor to find.
        
    Returns:
        ctypes.c_void_p: Pointer to the TreeNode containing the successor value, or None if no successor.
    """
    return lib.Successor_BinarySearchTree(tree, key)

# Insert
lib.Insert_BinarySearchTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Insert_BinarySearchTree.restype = None

def Insert(tree, key):
    """
    Insert a new key into the binary search tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the BST structure.
        key (int): The value to insert.
        
    Returns:
        None
    """
    lib.Insert_BinarySearchTree(tree, key)

# Delete
lib.Delete_BinarySearchTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Delete_BinarySearchTree.restype = None

def Delete(tree, key):
    """
    Delete a key from the binary search tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the BST structure.
        key (int): The value to delete.
        
    Returns:
        None
    """
    lib.Delete_BinarySearchTree(tree, key)

# Depth
lib.Depth_BinarySearchTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Depth_BinarySearchTree.restype = ctypes.c_int

def Depth(tree, key):
    """
    Get the depth of a specific key in the binary search tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the BST structure.
        key (int): The value whose depth to find.
        
    Returns:
        int: The depth of the node (distance from root), or -1 if key not found.
    """
    return lib.Depth_BinarySearchTree(tree, key)

# Height
lib.Height_BinarySearchTree.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Height_BinarySearchTree.restype = ctypes.c_int

def Height(tree, key):
    """
    Get the height of a specific node in the binary search tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the BST structure.
        key (int): The value whose height to find.
        
    Returns:
        int: The height of the node (distance to furthest leaf), or -1 if key not found.
    """
    return lib.Height_BinarySearchTree(tree, key)

# InOrder
lib.InOrder_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.InOrder_BinarySearchTree.restype = None

def InOrder(tree):
    """
    Perform inorder traversal of the binary search tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the BST structure.

    Returns:
        None
    """
    lib.InOrder_BinarySearchTree(tree)

# PreOrder
lib.PreOrder_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.PreOrder_BinarySearchTree.restype = None

def PreOrder(tree):
    """
    Perform preorder traversal of the binary search tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the BST structure.

    Returns:
        None
    """
    lib.PreOrder_BinarySearchTree(tree)

# PostOrder
lib.PostOrder_BinarySearchTree.argtypes = [ctypes.c_void_p]
lib.PostOrder_BinarySearchTree.restype = None

def PostOrder(tree):
    """
    Perform postorder traversal of the binary search tree.
    
    Args:
        tree (ctypes.c_void_p): Pointer to the BST structure.

    Returns:
        None
    """
    lib.PostOrder_BinarySearchTree(tree)
