import networkx as nx
import matplotlib.pyplot as plt

# Create a graph 
edges = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3]]
G = nx.Graph()
G.add_edges_from(edges)

# Degree Counting 
def count_degree(node):
    return G.degree[node]

node = 1
degree = count_degree(node)
print("Degree of node 1:", degree)

# Traversal DFS 
def dfs(node, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    
    if node not in visited:
        visited.add(node)
        result.append(node)
        for neighbor in G.neighbors(node):
            dfs(neighbor, visited, result)
    return result

dfs_result = dfs(1)
print("DFS Traversal from node 1:", dfs_result)

# Traversal BFS 
def bfs(node):
    visited = set()
    queue = [node]
    result = []
    
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            visited.add(current_node)
            result.append(current_node)
            queue.extend(n for n in G.neighbors(current_node) if n not in visited)
    return result

bfs_result = bfs(1)
print("BFS Traversal from node 1:", bfs_result)

# Shortest Path 
def find_shortest_path(source, target):
    try:
        return nx.shortest_path(G, source=source, target=target)
    except nx.NetworkXNoPath:
        return []

source, target = 1, 4
shortest_path = find_shortest_path(source, target)
print("Shortest path from 1 to 4:", shortest_path)

# Visualize  graph 
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)  
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        edge_color='gray', node_size=2000, font_size=12)
plt.title("Graph Visualization")
plt.tight_layout()
plt.savefig("graph.png")  
plt.show()
