import os
import ctypes
from DataStructures_py.Node import Node

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../Build/dstructures.so"))

# --- C Library Signatures ---
lib.Create_linkedlist.argtypes = []
lib.Create_linkedlist.restype = ctypes.c_void_p

lib.Destroy_linkedlist.argtypes = [ctypes.c_void_p]
lib.Destroy_linkedlist.restype = None

lib.GetHead_linkedlist.argtypes = [ctypes.c_void_p]
lib.GetHead_linkedlist.restype = ctypes.c_void_p

lib.Insert_linkedlist.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Insert_linkedlist.restype = None

lib.InsertLast_linkedlist.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.InsertLast_linkedlist.restype = None

lib.Delete_linkedlist.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.Delete_linkedlist.restype = None

lib.IsEmpty_linkedlist.argtypes = [ctypes.c_void_p]
lib.IsEmpty_linkedlist.restype = ctypes.c_bool

lib.Size_linkedlist.argtypes = [ctypes.c_void_p]
lib.Size_linkedlist.restype = ctypes.c_int

lib.Display_linkedlist.argtypes = [ctypes.c_void_p]
lib.Display_linkedlist.restype = None

class LinkedList:
    """
    LinkedList operations for dynamic data structures.

    This module provides Python wrappers for C++ linked list operations.
    All operations are encapsulated within the LinkedList class.
    """
    def __init__(self, ptr: ctypes.c_void_p = None) -> None:
        if ptr is not None:
            self.ptr = ptr
        else:
            self.ptr = lib.Create_linkedlist()

    def __del__(self) -> None:
        """Automatically destroy the list when the object is collected."""
        if hasattr(self, 'ptr') and self.ptr:
            lib.Destroy_linkedlist(self.ptr)
            self.ptr = None

    def GetHead(self) -> Node | None:
        """Get the head node as a Node instance (not owned)."""
        ptr = lib.GetHead_linkedlist(self.ptr)
        return Node(ptr=ptr, owned=False) if ptr else None

    def Insert(self, value: int) -> None:
        """Insert a value at the beginning of the list."""
        lib.Insert_linkedlist(self.ptr, value)

    def InsertLast(self, value: int) -> None:
        """Insert a value at the end of the list."""
        lib.InsertLast_linkedlist(self.ptr, value)

    def Delete(self, value: int) -> None:
        """Delete the first occurrence of a value."""
        lib.Delete_linkedlist(self.ptr, value)

    def IsEmpty(self) -> bool:
        """Check if the list is empty."""
        return lib.IsEmpty_linkedlist(self.ptr)

    def Size(self) -> int:
        """Get the number of elements in the list."""
        return lib.Size_linkedlist(self.ptr)

    def Display(self) -> None:
        """Display the list elements to the console."""
        lib.Display_linkedlist(self.ptr)