"""
TreeNode operations for tree data structures.

This module provides Python wrappers for C++ tree node operations including
creation and data access for binary trees, AVL trees, and other tree structures.
"""
import os
import ctypes

INT_MIN = -2147483648  # Minimum value for a 32-bit signed integer

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# Create
lib.Create_treenode.argtypes = [ctypes.c_int]
lib.Create_treenode.restype = ctypes.c_void_p

def Create(value):
    """
    Create a new tree node with the specified value.
    
    Args:
        value (int): The integer value to store in the tree node.
        
    Returns:
        ctypes.c_void_p: A pointer to the created tree node.
    """

    return lib.Create_treenode(value)

# Destroy
lib.Destroy_treenode.argtypes = [ctypes.c_void_p]
lib.Destroy_treenode.restype = None

def Destroy(node):
    """
    Destroy the tree node and free its memory.
    
    Args:
        node (ctypes.c_void_p): Pointer to the tree node to destroy.
        
    Returns:
        None
    """
    lib.Destroy_treenode(node)

# GetData
lib.GetData_treenode.argtypes = [ctypes.c_void_p]
lib.GetData_treenode.restype = ctypes.c_int

def GetData(node):
    """
    Get the data value stored in a tree node.
    
    Args:
        node (ctypes.c_void_p): Pointer to the tree node.

    Returns:
        int: The integer value stored in the tree node.
    """
    data = lib.GetData_treenode(node)
    if data == INT_MIN:
        return "No Data"
    return data

# GetRight
lib.GetRight_treenode.argtypes = [ctypes.c_void_p]
lib.GetRight_treenode.restype = ctypes.c_void_p

def GetRight(node):
    """
    Get the right child of a tree node.
    
    Args:
        node (ctypes.c_void_p): Pointer to the parent tree node.

    Returns:
        ctypes.c_void_p: Pointer to the right child node, or None if no right child.
    """

    return lib.GetRight_treenode(node)

# GetLeft
lib.GetLeft_treenode.argtypes = [ctypes.c_void_p]
lib.GetLeft_treenode.restype = ctypes.c_void_p

def GetLeft(node):
    """
    Get the left child of a tree node.
    
    Args:
        node (ctypes.c_void_p): Pointer to the parent tree node.

    Returns:
        ctypes.c_void_p: Pointer to the left child node, or None if no left child.
    """

    return lib.GetLeft_treenode(node)

# GetParent
lib.GetParent_treenode.argtypes = [ctypes.c_void_p]
lib.GetParent_treenode.restype = ctypes.c_void_p

def GetParent(node):
    """
    Get the parent node of a tree node.
    
    Args:
        node (ctypes.c_void_p): Pointer to the child tree node.

    Returns:
        ctypes.c_void_p: Pointer to the parent node, or None if node is root or has no parent.
    """

    return lib.GetParent_treenode(node)

# SetData
lib.SetData_treenode.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.SetData_treenode.restype = None

def SetData(node, value):
    """
    Set the data value of a tree node.
    
    Args:
        node (ctypes.c_void_p): Pointer to the tree node to modify.
        value (int): The new integer value to store in the node.
        
    Returns:
        None
    """

    lib.SetData_treenode(node, value)

# SetRight
lib.SetRight_treenode.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.SetRight_treenode.restype = None

def SetRight(node, right):
    """
    Set the right child of a tree node.
    
    Args:
        node (ctypes.c_void_p): Pointer to the parent tree node.
        right (ctypes.c_void_p): Pointer to the node that should become the right child,
                               or None to remove the right child.
        
    Returns:
        None
    """

    lib.SetRight_treenode(node, right)

# SetLeft
lib.SetLeft_treenode.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.SetLeft_treenode.restype = None

def SetLeft(node, left):
    """
    Set the left child of a tree node.
    
    Args:
        node (ctypes.c_void_p): Pointer to the parent tree node.
        left (ctypes.c_void_p): Pointer to the node that should become the left child,
                              or None to remove the left child.
        
    Returns:
        None
    """

    lib.SetLeft_treenode(node, left)

# SetParent
lib.SetParent_treenode.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.SetParent_treenode.restype = None

def SetParent(node, parent):
    """
    Set the parent node of a tree node.
    
    Args:
        node (ctypes.c_void_p): Pointer to the child tree node.
        parent (ctypes.c_void_p): Pointer to the node that should become the parent,
                                or None to make this node a root.
        
    Returns:
        None
    """
    lib.SetParent_treenode(node, parent)