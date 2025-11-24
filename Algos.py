"""
A Python module for interacting with a C++ library that provides algorithms.
"""
import os
import ctypes

# Load the library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "Build/algos.so"))

# InsertionSort
lib.InsertionSort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
lib.InsertionSort.restype = None

def InsertionSort(array):
    """
    Sort an array using the insertion sort algorithm.
    
    Args:
        array (list[int]): List of integers to sort.
        
    Returns:
        list[int]: A new sorted list (original list is not modified).
        
    Time Complexity:
        - Best case: O(n) when array is already sorted
        - Average/Worst case: O(n²)
    """

    c_array = (ctypes.c_int * len(array))(*array)
    lib.InsertionSort(c_array, len(array))
    return list(c_array)

# MergeSort
lib.MergeSort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
lib.MergeSort.restype = None

def MergeSort(array):
    """
    Sort an array using the merge sort algorithm.
    
    Args:
        array (list[int]): List of integers to sort.
        
    Returns:
        list[int]: A new sorted list (original list is not modified).
        
    Time Complexity:
        - All cases: O(n log n)
        
    Space Complexity:
        - O(n) auxiliary space
    """
    
    c_array = (ctypes.c_int * len(array))(*array)
    lib.MergeSort(c_array, 0, len(array) - 1)
    return list(c_array)

# QuickSort
lib.QuickSort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
lib.QuickSort.restype = None 

def QuickSort(array):
    """
    Sort an array using the quick sort algorithm.
    
    Args:
        array (list[int]): List of integers to sort.
        
    Returns:
        list[int]: A new sorted list (original list is not modified).
        
    Time Complexity:
        - Best case: O(n log n) when pivot divides array evenly
        - Average case: O(n log n)
        - Worst case: O(n²) when pivot is always the smallest or largest element
        
    Space Complexity:
        - O(log n) auxiliary space for recursion stack in best/average case
        - O(n) auxiliary space in worst case
    """
    c_array = (ctypes.c_int * len(array))(*array)
    lib.QuickSort(c_array, 0, len(array) - 1)
    return list(c_array)

# CountingSort
lib.CountingSort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
lib.CountingSort.restype = None

def CountingSort(array):
    """
    Sort an array using the counting sort algorithm.
    
    Args:
        array (list[int]): List of non-negative integers to sort.
        
    Returns:
        list[int]: A new sorted list (original list is not modified), or None if input contains negative numbers.
        
    Time Complexity:
        - All cases: O(n + k) where n is the number of elements and k is the range of input
        
    Space Complexity:
        - O(k) auxiliary space where k is the range of input values
        
    Note:
        Counting sort is a non-comparison based sorting algorithm that works only
        with non-negative integers.
    """
    if(len(array) == 0):
        return []

    max_item = max(array)
    min_item = min(array)

    if(min_item < 0):
        print("CountingSort only works for non-negative integers.")
        return None
    
    temp_array = [-1 for i in range(len(array))]
    
    c_array = (ctypes.c_int * len(array))(*array)
    c_array_temp = (ctypes.c_int * len(temp_array))(*temp_array)
    lib.CountingSort(c_array, c_array_temp, max_item, len(array))
    return list(c_array_temp)

