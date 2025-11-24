# Data Structures & Algorithms Libraries

A comprehensive, high-performance algorithms and data structures library featuring both Python and C++ implementations. This library provides efficient, well-documented implementations of essential computer science algorithms and data structures with seamless Python-C++ integration.

## Features

- **Dual Implementation**: Both Python and C++ versions for flexibility and performance
- **High Performance**: C++ backend with Python wrappers using ctypes for optimal speed
- **Comprehensive Coverage**: Wide range of algorithms and data structures
- **Memory Safe**: Automatic memory management with clear ownership semantics
- **Well Documented**: Detailed docstrings with time/space complexity analysis
- **Easy to Use**: Simple, intuitive Python API

## What's Included
### [Algorithms (`Algos.py`)](Algos.py)

#### Sorting Algorithms
- **Insertion Sort** - O(n²) simple sorting algorithm, efficient for small datasets
- **Merge Sort** - O(n log n) stable divide-and-conquer sorting
- **Quick Sort** - O(n log n) average case, efficient in-place sorting
- **Counting Sort** - O(n + k) non-comparison based sorting for integers

### [Data Structures (`DataStructures.py`)](DataStructures.py)

#### Linear Data Structures
- **LinkedList** - Dynamic list with efficient insertion/deletion
- **Stack** - LIFO (Last In, First Out) structure
- **Queue** - FIFO (First In, First Out) structure
- **PriorityQueue** - Heap-based priority queue (max-heap implementation)

#### Tree Data Structures
- **BinarySearchTree** - Ordered tree structure with O(log n) average operations
- **AVLTree** - Self-balancing BST guaranteeing O(log n) operations
- **TreeNode** - Supporting node structure for tree implementations

#### Advanced Data Structures
- **SkipList** - Probabilistic data structure with O(log n) expected performance
- **Graph** - Supports both directed and undirected graphs with various algorithms

#### Supporting Components
- **Node** - Basic node structure for linked data structures
- **SkipListNode** - Specialized node for skip list implementation
- **GraphVertex** & **Edge** - Graph components for vertex and edge operations

## Memory Management

⚠️ **CRITICAL**: This library uses C++ backend with manual memory management. Always call `Destroy()` functions to prevent memory leaks.

### Memory Management Rules
1. **All data structures** must be destroyed: `LinkedList.Destroy()`, `Stack.Destroy()`, `Graph.Destroy()`, etc.
2. **Standalone nodes** must be destroyed: `Node.Destroy()`, `TreeNode.Destroy()`, `SkipListNode.Destroy()`
3. **Graph returned objects** need special cleanup: `Graph.DestroyReturnedLinkedList()`
4. **GetNeighbors()** returns internal pointers - do NOT delete these

### Basic Memory Management Pattern
```python
# Create → Use → Destroy pattern
data_structure = DataStructure.Create()
try:
    # Use the data structure
    DataStructure.SomeOperation(data_structure, value)
finally:
    DataStructure.Destroy(data_structure)  # ALWAYS cleanup!
```

## Quick Start

### Prerequisites
- Python 3.x
- C++ compiler (for building from source)
- Linux/Unix environment (for shared library support)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/hadar88/DSAlgo.git
cd DSAlgo
```

2. **The library comes pre-built with compiled shared libraries in the `Build/` directory**

### Basic Usage

#### Using Sorting Algorithms
```python
import Algos

# Example array
numbers = [64, 34, 25, 12, 22, 11, 90]

# Quick Sort
sorted_numbers = Algos.QuickSort(numbers)
print(f"Sorted: {sorted_numbers}")
```

#### Using Data Structures
```python
from DataStructures import Stack, BinarySearchTree, TreeNode

# Create and use a Stack
stack = Stack.Create()
Stack.Push(stack, 10)
Stack.Push(stack, 20)
value = Stack.Pop(stack)
print(value)  # Outputs: 20
Stack.Destroy(stack)  # Clean up the stack

# Create and use a Binary Search Tree
bst = BinarySearchTree.Create()
BinarySearchTree.Insert(bst, 50)
BinarySearchTree.Insert(bst, 30)
BinarySearchTree.Insert(bst, 70)

# Search for a value
found = BinarySearchTree.Search(bst, 30)
if found:
    print(TreeNode.GetData(found))  # Outputs: 30
BinarySearchTree.Destroy(bst)  # Clean up the BST
```

#### Working with Graphs
```python
from DataStructures import Graph

# Create a directed graph
graph = Graph.Create(directed=True)

# Add vertices and edges
Graph.CreateVertex(graph, 1)
Graph.CreateVertex(graph, 2)
Graph.CreateVertex(graph, 3)

Graph.AddEdge(graph, 1, 2)  # Edge from 1 to 2
Graph.AddEdge(graph, 2, 3)  # Edge from 2 to 3
Graph.AddEdge(graph, 1, 3)  # Edge from 1 to 3

# Perform graph algorithms
Graph.PrintPath(graph, 1, 3)  # Shortest path from vertex 1 to 3
Graph.Destroy(graph)  # Clean up the graph
```

### Special Graph Cleanup Rules
- `Graph.GetVertices()` → `Graph.DestroyReturnedLinkedList(vertices)`
- `Graph.GetReachableVertices()` → `Graph.DestroyReturnedLinkedList(reachable)`
- `Graph.GetNeighbors()` → **Do NOT destroy** (internal pointer)

## Project Structure

```
DSAlgo/
├── Algos.py                    # Main algorithms module
├── DataStructures.py           # Main data structures module
├── Build/                      # Compiled C++ libraries
│   ├── algos.so                # Algorithms shared library
│   ├── algos.cpp               # Algorithms C++ source
│   ├── dstructures.so          # Data structures shared library
│   ├── dstructures.cpp         # Data structures C++ source
│   └── dstructures.h           # Data structures C++ header
├── DataStructures_py/          # Python implementations
│   ├── LinkedList.py
│   ├── Stack.py
│   ├── Queue.py
│   ├── BinarySearchTree.py
│   ├── AVLTree.py
│   ├── Graph.py
│   └── ...
└── DataStructures_cpp/         # C++ implementations
    ├── LinkedList.cpp
    ├── Stack.cpp
    ├── Queue.cpp
    └── ...
```

## Performance Characteristics

| Algorithm/Data Structure | Time Complexity | Space Complexity |
|--------------------------|----------------|------------------|
| Merge Sort | O(n log n) | O(n) |
| Quick Sort | O(n log n) avg, O(n²) worst | O(log n) avg, O(n) worst |
| LinkedList Insert/Delete | O(1) at head, O(n) at position | O(1) per node |
| Stack Push/Pop | O(1) | O(1) per operation |
| Queue Enqueue/Dequeue | O(1) | O(1) per operation |
| BST Operations | O(log n) avg, O(n) worst | O(n) total |
| AVL Tree Operations | O(log n) guaranteed | O(n) total |
| Skip List Operations | O(log n) expected | O(n) expected |
| Graph BFS | O(V + E) | O(V) |

## Advanced Features

### Memory Management
- Automatic memory management for Python interface
- Efficient C++ backend with proper resource cleanup
- Safe pointer handling through ctypes

### Error Handling
- Comprehensive input validation
- Graceful handling of edge cases
- Detailed error messages and documentation

### Extensibility
- Modular design for easy extension
- Clear separation between Python wrapper and C++ implementation
- Well-defined interfaces for adding new algorithms

## Known Issues

- Shared libraries are compiled for Linux/Unix systems
- Windows users may need to recompile the C++ libraries

## Author

**Hadar** - [GitHub Profile](https://github.com/hadar88)

## Acknowledgments

- Inspired by classic computer science algorithms and data structures
- Built with performance and educational value in mind
- Designed for both learning and production use

---

**If you find this library helpful, please consider giving it a star!**