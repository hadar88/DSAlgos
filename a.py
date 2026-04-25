from algos_structs import Graph, MST
import time

g = Graph(False)

g.CreateVertex(1)
g.CreateVertex(2)
g.CreateVertex(3)
g.CreateVertex(4)
g.CreateVertex(5)
g.CreateVertex(6)
g.CreateVertex(7)
g.CreateVertex(8)
g.CreateVertex(9)

g.CreateWeightedEdge(1, 2, 4)
g.CreateWeightedEdge(1, 3, 8)
g.CreateWeightedEdge(2, 3, 11)
g.CreateWeightedEdge(2, 5, 8)
g.CreateWeightedEdge(3, 4, 7)
g.CreateWeightedEdge(3, 6, 1)
g.CreateWeightedEdge(4, 5, 2)
g.CreateWeightedEdge(4, 6, 6)
g.CreateWeightedEdge(5, 7, 7)
g.CreateWeightedEdge(5, 8, 4)
g.CreateWeightedEdge(6, 8, 2)
g.CreateWeightedEdge(7, 8, 14)
g.CreateWeightedEdge(7, 9, 9)
g.CreateWeightedEdge(8, 9, 10)

kruskal_start = time.perf_counter()
kruskal = MST.Kruskal(g)
kruskal_end = time.perf_counter()

prim_start = time.perf_counter()
prim = MST.Prim(g)
prim_end = time.perf_counter()

print(f"Kruskal's algorithm took: {kruskal_end - kruskal_start} seconds")
print(f"Prim's algorithm took: {prim_end - prim_start} seconds")
print(
    f"The difference is {((kruskal_end - kruskal_start) - (prim_end - prim_start))} seconds"
)
