"""
Sort algorithms operations.

This module provides Python wrappers for C++ sort operations including
insertion sort, merge sort, quick sort, and counting sort.
"""
import os
import ctypes

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "algos.so"))

# --- C Library Signatures ---
lib.Insertion.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
lib.Insertion.restype = None

lib.Merge.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
lib.Merge.restype = None

lib.Quick.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
lib.Quick.restype = None

lib.Counting.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
lib.Counting.restype = None

class Sorts:
    """A collection of sorting algorithms wrapped from C++."""

    @staticmethod
    def InsertionSort(array: list[int]) -> list[int]:
        """
        Sort an array using the insertion sort algorithm.

        Parameters
        ----------
        array : list[int]
            List of integers to sort.

        Returns
        -------
        list[int]
            A new sorted list (original list is not modified).

        Notes
        -----
        - Time complexity: Best: O(n), Average: O(n^2), Worst: O(n^2)
        - Space complexity: O(1) auxiliary space
        """
        if not array:
            return []
        c_array = (ctypes.c_int * len(array))(*array)
        lib.Insertion(c_array, len(array))
        return list(c_array)

    @staticmethod
    def MergeSort(array: list[int]) -> list[int]:
        """
        Sort an array using the merge sort algorithm.

        Parameters
        ----------
        array : list[int]
            List of integers to sort.

        Returns
        -------
        list[int]
            A new sorted list (original list is not modified).

        Notes
        -----
        - Time complexity: O(n log n)
        - Space complexity: O(n) auxiliary space
        """
        if not array:
            return []
        c_array = (ctypes.c_int * len(array))(*array)
        lib.Merge(c_array, 0, len(array) - 1)
        return list(c_array)

    @staticmethod
    def QuickSort(array: list[int]) -> list[int]:
        """
        Sort an array using the quick sort algorithm.
        
        Parameters
        ----------
        array : list[int]
            List of integers to sort.
            
        Returns
        -------
        list[int]
            A new sorted list (original list is not modified).
            
        Notes
        -----
        - Time complexity: Best: O(n log n), Average: O(n log n), Worst: O(n^2)
        - Space complexity: O(log n) auxiliary space for recursion stack in best/average case, O(n) auxiliary space in worst case
        """
        if not array:
            return []
        c_array = (ctypes.c_int * len(array))(*array)
        lib.Quick(c_array, 0, len(array) - 1)
        return list(c_array)

    @staticmethod
    def CountingSort(array: list[int]) -> list[int] | None:
        """
        Sort an array using the counting sort algorithm.
        
        Parameters
        ----------
        array : list[int]
            List of non-negative integers to sort.
            
        Returns
        -------
        list[int]
            A new sorted list (original list is not modified), or None if input contains negative numbers.
            
        Notes
        -----
        - Time complexity: O(n + k) where n is the number of elements and k is the range of input
        - Space complexity: O(k) auxiliary space where k is the range of input values
        - Counting sort is a non-comparison based sorting algorithm that works only
            with non-negative integers.
        """
        if not array:
            return []

        max_item = max(array)
        min_item = min(array)

        if min_item < 0:
            print("CountingSort only works for non-negative integers.")
            return None
        
        temp_array = [-1 for i in range(len(array))]
        
        c_array = (ctypes.c_int * len(array))(*array)
        c_array_temp = (ctypes.c_int * len(temp_array))(*temp_array)
        lib.Counting(c_array, c_array_temp, max_item, len(array))
        return list(c_array_temp)