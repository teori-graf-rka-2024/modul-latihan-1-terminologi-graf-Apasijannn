import networkx as nx
import matplotlib.pyplot as plt

# Create graph
def create_graph(edges:list[tuple[int, int]]) -> nx.Graph:
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

# Degree Counting
def get_degree(G: nx.Graph, node: int) -> int:
    return G.degree[node]

# Traversal DFS
def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return list(nx.dfs_preorder_nodes(G, start))

# Traversal BFS
def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return list(nx.bfs_tree(G, source=start))

# Shortest path
def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    return nx.shortest_path(G, source=source, target=target)

# Visualize graph
def visualize_graph(G: nx.Graph) -> None:
    nx.draw(G)
    plt.show()
