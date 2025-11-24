"""
Stack operations for LIFO (Last In, First Out) data structures.

This module provides Python wrappers for C++ stack operations including
creation, push, pop, and checking if the stack is empty. The stack follows
the LIFO principle where elements are added and removed from the top.
"""
import os
import ctypes

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# Create
lib.Create_stack.argtypes = []
lib.Create_stack.restype = ctypes.c_void_p

def Create():
    """
    Create a new empty stack.
    
    Returns:
        ctypes.c_void_p: A pointer to the stack structure.
    """
    return lib.Create_stack()

# Destroy
lib.Destroy_stack.argtypes = [ctypes.c_void_p]
lib.Destroy_stack.restype = None

def Destroy(stack):
    """
    Destroy the stack and free its memory.

    Args:
        stack (ctypes.c_void_p): Pointer to the stack structure.

    Returns:
        None
    """
    if stack:
        lib.Destroy_stack(stack)

# IsEmpty
lib.IsEmpty_stack.argtypes = [ctypes.c_void_p]
lib.IsEmpty_stack.restype = ctypes.c_bool

def IsEmpty(stack):
    """
    Check if the stack is empty.
    
    Args:
        stack (ctypes.c_void_p): Pointer to the stack structure.

    Returns:
        bool: True if the stack is empty (no elements), False otherwise.
    """
    return lib.IsEmpty_stack(stack)

# Push
lib.Push_stack.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Push_stack.restype = None

def Push(stack, value):
    """
    Push a new value onto the top of the stack.
    
    Args:
        stack (ctypes.c_void_p): Pointer to the stack structure.
        value (int): The integer value to push onto the stack.
        
    Returns:
        None
    """
    lib.Push_stack(stack, value)

# Pop
lib.Pop_stack.argtypes = [ctypes.c_void_p]
lib.Pop_stack.restype = ctypes.c_int

def Pop(stack):
    """
    Remove and return the top element from the stack.
    
    Args:
        stack (ctypes.c_void_p): Pointer to the stack structure.

    Returns:
        int: The value that was at the top of the stack.
    """
    return lib.Pop_stack(stack)

# Display

lib.Display_stack.argtypes = [ctypes.c_void_p]
lib.Display_stack.restype = None

def Display(stack):
    """
    Display all elements in the stack to console.
    
    Args:
        stack (ctypes.c_void_p): Pointer to the stack structure.

    Returns:
        None
    """
    lib.Display_stack(stack)