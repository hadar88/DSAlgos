"""
Stack operations for LIFO (Last In, First Out) data structures.

This module provides Python wrappers for C++ stack operations.
All operations are encapsulated within the Stack class.
"""
import os
import ctypes

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# --- C Library Signatures ---
lib.Create_stack.argtypes = []
lib.Create_stack.restype = ctypes.c_void_p

lib.Destroy_stack.argtypes = [ctypes.c_void_p]
lib.Destroy_stack.restype = None

lib.IsEmpty_stack.argtypes = [ctypes.c_void_p]
lib.IsEmpty_stack.restype = ctypes.c_bool

lib.Push_stack.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Push_stack.restype = None

lib.Pop_stack.argtypes = [ctypes.c_void_p]
lib.Pop_stack.restype = ctypes.c_int

lib.Display_stack.argtypes = [ctypes.c_void_p]
lib.Display_stack.restype = None

class Stack:
    """A thin wrapper around a C++ stack pointer."""
    def __init__(self, ptr: ctypes.c_void_p = None) -> None:
        if ptr is not None:
            self.ptr = ptr
        else:
            self.ptr = lib.Create_stack()

    def __del__(self) -> None:
        """Automatically destroy the stack when the object is collected."""
        if hasattr(self, 'ptr') and self.ptr:
            lib.Destroy_stack(self.ptr)
            self.ptr = None

    def IsEmpty(self) -> bool:
        """Check if the stack is empty."""
        return lib.IsEmpty_stack(self.ptr)

    def Push(self, value: int) -> None:
        """Push a value onto the top of the stack."""
        lib.Push_stack(self.ptr, value)

    def Pop(self) -> int:
        """Remove and return the top element from the stack."""
        return lib.Pop_stack(self.ptr)

    def Display(self) -> None:
        """Display all elements in the stack to console."""
        lib.Display_stack(self.ptr)