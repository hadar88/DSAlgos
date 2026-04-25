# DSAlgos: Data Structures & Algorithms Library

A comprehensive, high-performance algorithms and data structures library featuring Python object-oriented interfaces backed by fast C++ implementations. This library provides efficient, well-documented implementations of essential computer science algorithms and data structures with seamless Python-C++ integration.

## Features

- **High Performance**: C++ backend with Python wrappers using ctypes for optimal speed.
- **Object-Oriented Python API**: Clean, intuitive class-based interfaces in Python.
- **Memory Safe**: Automatic memory management via Python's garbage collection (`__del__` bindings).
- **Comprehensive Coverage**: Wide range of algorithms (sorting, minimum spanning trees) and data structures (trees, graphs, lists).
- **Dual Support**: Supports directed and undirected, weighted and unweighted graphs.

## What's Included

### Algorithms

#### Sorting (`Sorts`)
- **Insertion Sort** - $O(n^2)$ simple sorting algorithm
- **Merge Sort** - $O(n \log n)$ stable divide-and-conquer
- **Quick Sort** - $O(n \log n)$ average case
- **Counting Sort** - $O(n + k)$ non-comparison based for integers

#### Minimum Spanning Trees (`MST`)
- **Kruskal's Algorithm**
- **Prim's Algorithm**

### Data Structures

#### Linear Data Structures
- **LinkedList** - Dynamic list with efficient operations
- **Stack** - LIFO structure
- **Queue** - FIFO structure
- **PriorityQueue** - Heap-based priority queue

#### Tree Data Structures
- **BinarySearchTree** - Ordered tree
- **AVLTree** - Self-balancing BST
- **TreeNode** - Supporting node structure

#### Advanced Data Structures
- **SkipList** - Probabilistic data structure
- **Graph** - Supports directed/undirected, weighted/unweighted graphs with BFS, pathfinding, etc.
- **DisjointSets** - Union-find data structure

#### Supporting Components
- **Node**, **SkipListNode**, **DisjointSetsItem** - Component nodes

## Quick Start

### Prerequisites
- Python 3.10+
- C++ compiler (`g++`)
- Linux/Unix environment (or WSL for Windows users) for building shared libraries

### Installation

**Install from PyPI (Recommended)**
The easiest way to install the library is directly from PyPI:
```bash
pip install algos-structs
```

**Build from Source**
If you want to modify the library or build it locally:

1. **Clone the repository:**
```bash
git clone https://github.com/hadar88/DSAlgo.git
cd DSAlgo
```

2. **Build and install locally:**
Run the provided build script to compile the C++ shared libraries and install the Python package. This script also sets up the correct `.whl` distribution.
```bash
./build.sh
```
*(Optional)* If you are developing on WSL and want the package installed into your Windows Python environment as well (useful for VS Code IntelliSense), add the `--windows` flag:
```bash
./build.sh --windows
```

### Publishing to PyPI

You can automatically build and upload your package to PyPI using the build script. 

1. Create a `.env` file in the project root with your PyPI credentials:
```env
TWINE_USERNAME="__token__"
TWINE_PASSWORD="pypi-your-token-here"
```

2. Run the build script with the upload flag:
```bash
./build.sh --upload
```
*(Note: You can combine flags, e.g., `./build.sh --upload --windows`)*

This will compile the libraries, package the wheel, securely upload it to PyPI without prompting for a password, and then automatically install the newly published version directly from PyPI.

### Basic Usage

#### Using Sorting Algorithms
```python
from algos_structs import Sorts

# Example array
numbers = [64, 34, 25, 12, 22, 11, 90]

# Quick Sort
sorted_numbers = Sorts.QuickSort(numbers)
print(f"Sorted: {sorted_numbers}")
```

#### Using Data Structures
```python
from algos_structs import Stack, BinarySearchTree

# Create and use a Stack
stack = Stack()
stack.Push(10)
stack.Push(20)
value = stack.Pop()
print(value)  # Outputs: 20
# Memory is automatically cleaned up when `stack` goes out of scope

# Create and use a Binary Search Tree
bst = BinarySearchTree()
bst.Insert(50)
bst.Insert(30)
bst.Insert(70)

# Search for a value
found = bst.Search(30)
if found:
    print(found.GetData())  # Outputs: 30
```

#### Working with Graphs and Algorithms
```python
from algos_structs import Graph, MST

# Create an undirected graph
g = Graph(directed=False)

# Add vertices and weighted edges
for i in range(1, 5):
    g.CreateVertex(i)

g.CreateWeightedEdge(1, 2, 4.0)
g.CreateWeightedEdge(2, 3, 3.0)
g.CreateWeightedEdge(1, 3, 8.0)
g.CreateWeightedEdge(3, 4, 7.0)

# Perform Breadth-First Search
colors, distances, parents = g.BFS(1)
print(f"Distances from vertex 1: {distances}")

# Find Minimum Spanning Tree using Kruskal's algorithm
mst = MST.Kruskal(g)
```

## Project Structure

```
algos_structs/
├── src/
│   └── algos_structs/           # Python package
│       ├── __init__.py          # Exposes the main API
│       ├── Algos/               # Algorithm wrappers (Sorts, MST)
│       │   └── algos.so         # Compiled C++ algorithms library
│       └── DataStructures/      # Data structure wrapper classes
│           └── dstructures.so   # Compiled C++ data structures library
├── Build/                       # C++ source code for shared libraries
│   ├── algos.cpp
│   └── dstructures.cpp
├── build.sh                     # Build and installation script
└── pyproject.toml               # Python package configuration
```

## Advanced Features

### Memory Management
- **Python Garbage Collection**: The Python classes implement `__del__` to automatically free underlying C++ resources when the objects are no longer needed.
- **Resource Cleanup**: Prevents memory leaks by ensuring the C++ structures are properly destroyed.

### C++ Integration
- Uses Python's `ctypes` library to directly interact with highly optimized C++ code.

## Known Issues

- Shared libraries (`.so`) are compiled for Linux/Unix/WSL systems.
- Windows users should run the code through WSL or recompile the libraries as `.dll` files.

## Author

**Hadar** - [GitHub Profile](https://github.com/hadar88)

## Acknowledgments

- Inspired by classic computer science algorithms and data structures
- Built with performance and educational value in mind
- Designed for both learning and production use

---

**If you find this library helpful, please consider giving it a star!**