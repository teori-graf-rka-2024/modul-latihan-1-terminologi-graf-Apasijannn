import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Tuple

# Membuat graf tidak berarah
edges = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]
G = nx.Graph()
G.add_edges_from(edges)

# Menghitung derajat simpul tertentu
node = 1
degree = G.degree[node]
print("Degree of node 1:", degree)

# Traversal DFS
visited = set()
dfs_result = []

def dfs(node):
    if node not in visited:
        visited.add(node)
        dfs_result.append(node)
        for neighbor in G.neighbors(node):
            dfs(neighbor)

dfs(1)
print("DFS Traversal from node 1:", dfs_result)

# Traversal BFS
visited = set()
queue = [1]
bfs_result = []

while queue:
    node = queue.pop(0)
    if node not in visited:
        visited.add(node)
        bfs_result.append(node)
        queue.extend(n for n in G.neighbors(node) if n not in visited)

print("BFS Traversal from node 1:", bfs_result)

# Menemukan jalur terpendek
source, target = 1, 4
try:
    shortest_path = nx.shortest_path(G, source=source, target=target)
except nx.NetworkXNoPath:
    shortest_path = []

print("Shortest path from 1 to 4:", shortest_path)

# Visualisasi graf
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)
plt.show()
