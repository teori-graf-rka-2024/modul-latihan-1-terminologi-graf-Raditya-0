# tutorial.py
from graph import create_graph, get_degree, dfs_traversal, bfs_traversal, find_shortest_path, visualize_graph

edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 5), (2, 4)]
G = create_graph(edges)

print("Derajat node 2:", get_degree(G, 2))
print("DFS traversal dimulai dari node 1:", dfs_traversal(G, 1))
print("BFS traversal dimulai dari node 1:", bfs_traversal(G, 1))
print("path terpendek dari node 1 ke node 4:", find_shortest_path(G, 1, 4))

visualize_graph(G)
