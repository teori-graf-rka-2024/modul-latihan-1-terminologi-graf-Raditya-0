from graph import create_graph, get_degree, dfs_traversal, bfs_traversal, find_shortest_path, visualize_graph

# Daftar koneksi antar simpul
graph_edges = [(1, 2), (2, 3), (3, 4), (4, 1), (2, 5), (5, 6), (3, 6), (4, 7)]

# 1. Membentuk struktur graf
network = create_graph(graph_edges)
print(f"Total simpul: {len(network.nodes)}")
print(f"Total koneksi: {len(network.edges)}\n")

# 2. Menampilkan derajat tiap edge
nodes_to_check = [2, 5, 7]
for node in nodes_to_check:
    print(f"Derajat simpul {node}: {get_degree(network, node)}")
print()

# 3. Menjalankan DFS
dfs_output = dfs_traversal(network, 1)
print(f"Hasil DFS: {dfs_output}\n")

# 4. Menjalankan BFS
bfs_output = bfs_traversal(network, 1)
print(f"Hasil BFS: {bfs_output}\n")

# 5. Menemukan jalur terpendek
paths_to_check = [(1, 6), (3, 7), (1, 5)]  
for start, end in paths_to_check:
    path_result = find_shortest_path(network, start, end)
    if path_result:
        print(f"Jalur dari {start} ke {end}: {path_result}")
    else:
        print(f"Tidak ditemukan jalur dari {start} ke {end}")
print()

# 6. Memvisualisasikan graf
visualize_graph(network)
print("Graf telah divisualisasikan dan disimpan sebagai file.")
