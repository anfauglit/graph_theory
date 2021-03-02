import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

committes = []
with open('data.txt', 'r') as f:
	for line in f.readlines():
		committes.append(line.strip().split(','))

committes_flat = list(np.concatenate(committes).flat)
# print(committes_flat)
committe_members = np.unique(committes_flat)
# print(committe_members)
committes = list(map(set, committes))

committes_with_commons = []
for i, c in enumerate(committes):
	for j, d in enumerate(committes[i + 1:]):
		if len(c & d) > 0:
			committes_with_commons.append((i, i + j + 1))

# print(committes_with_commons)
			
G = nx.Graph()

G.add_nodes_from(range(len(committes)))
labels = dict([(x, x + 1) for x in range(len(committes))])

# print(G.nodes)
G.add_edges_from(committes_with_commons)
# print(G.edges)

H = nx.Graph()
H.add_nodes_from([2,3,5,8,13,21])
fibo_edges = []

for n in H.nodes:
	for m in H.nodes:
		if (n + m in H.nodes) or (abs(n - m) in H.nodes):
			if (m, n) not in fibo_edges:
				fibo_edges.append((n,m))

print(fibo_edges)
H.add_edges_from(fibo_edges)

graph_options = {
	'with_labels': False,
	'node_color': 'k',
	'edge_color': 'k',
}

label_options = {
	'font_color': 'w',
	'font_size': 10,
}

nx.draw(H, with_labels=True)
pos = nx.circular_layout(G)
# nx.draw_networkx_labels(G, pos, labels, **label_options) 
# nx.draw(G, pos, **graph_options)
plt.show()
