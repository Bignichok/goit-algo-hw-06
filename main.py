import networkx as nx
import matplotlib.pyplot as plt

from dfs import dfs
from bfs import bfs 
from dijkstra import dijkstra

G = nx.Graph()

cities = ['Vinnytsia', 'Khmelnytskyi', 'Ternopil', 'Bukovel', 'Chernyvtsi', 'Kyiv', 'Lviv', 'Odesa', 'Kharkiv', 'Dnipro', 'Zhytomyr', "Uman"]
G.add_nodes_from(cities)

roads = [
    ('Vinnytsia', 'Khmelnytskyi', 119),
    ('Vinnytsia', 'Uman', 161),
    ('Khmelnytskyi', 'Ternopil', 112),
    ('Khmelnytskyi', 'Chernyvtsi', 189),
    ('Ternopil', 'Bukovel', 224),
    ('Bukovel', 'Chernyvtsi', 162),
    ('Kyiv', 'Lviv', 540),
    ('Kyiv', 'Kharkiv', 488),
    ('Kyiv', 'Dnipro', 484),
    ('Kyiv', 'Zhytomyr', 140),
    ('Kyiv', 'Uman', 211),
    ('Kharkiv', 'Dnipro', 210),
    ('Zhytomyr', 'Vinnytsia', 210),
    ('Zhytomyr', 'Khmelnytskyi', 190),
    ('Zhytomyr', 'Lviv', 403),
    ('Odesa', 'Uman', 271),
    ('Dnipro', 'Lviv', 580),
    ('Dnipro', 'Uman', 418),
]
G.add_weighted_edges_from(roads)

start_node = 'Vinnytsia'

dfs_result = dfs(G, start_node)
bfs_result = bfs(G, start_node)
shortest_paths = dijkstra(G, start_node)

def compare_paths(dfs_result, bfs_result):
    dfs_path = list(dfs_result)
    bfs_path = list(bfs_result)
    
    print(f"DFS шлях (порядок відвідування): {dfs_path}")
    print(f"BFS шлях (порядок відвідування): {bfs_path}")

compare_paths(dfs_result, bfs_result)

for destination in shortest_paths:
    path = []
    current_node = destination
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    path = path[::-1]
    print(f"Шлях з {start_node} до {destination}: {path} з загальною вагою {shortest_paths[destination][1]}")
    
# Візуалізація
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="purple", font_size=14, font_weight="bold", edge_color="gray")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Транспортна мережа України з вагами")
plt.show()

# Аналіз основних характеристик графа

# Кількість вершин та ребер
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")

# Ступінь вершин
degree_dict = dict(G.degree())
print("Ступінь кожної вершини:")
for node, degree in degree_dict.items():
    print(f"{node}: {degree}")

# Середній ступінь вершини
avg_degree = sum(degree_dict.values()) / num_nodes
print(f"Середній ступінь вершини: {avg_degree:.2f}")

# Аналіз компонентів зв'язності
connected_components = list(nx.connected_components(G))
num_connected_components = nx.number_connected_components(G)
print(f"Кількість компонентів зв'язності: {num_connected_components}")
print("Вершини в кожній компоненті зв'язності:")
for i, component in enumerate(connected_components):
    print(f"Компонента {i + 1}: {component}")
