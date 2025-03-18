import graph  # Mengimpor file graph.py yang telah dibuat sebelumnya

# Membuat graf dengan beberapa sisi
edges = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]
G = g.create_graph(edges)

# Menguji fungsi get_degree
print("Degree of node 1:", g.get_degree(G, 1))

# Menguji traversal DFS
print("DFS Traversal from node 1:", g.dfs_traversal(G, 1))

# Menguji traversal BFS
print("BFS Traversal from node 1:", g.bfs_traversal(G, 1))

# Menguji pencarian jalur terpendek
print("Shortest path from 1 to 4:", g.find_shortest_path(G, 1, 4))

# Visualisasi graf
g.visualize_graph(G)
