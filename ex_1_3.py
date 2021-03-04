import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import string
import itertools as it

def comp_words(word1, word2):
	singleton_presence = 0	
	letter_pairs = set((map(frozenset, zip(word1, word2))))
	for lp in letter_pairs:
		if len(lp) == 1:
			singleton_presence = singleton_presence + 1 

	if len(letter_pairs) == 2 and singleton_presence == 1:
		return True
	elif singleton_presence == 2:
		return True

	return False

G = nx.Graph()

graph_options = {
	'with_labels': False,
	'node_color': 'k',
	'edge_color': 'r',
	'node_size': 500,
}

label_options = {
	'font_color': 'w',
	'font_size': 12,
}

fig, ax = plt.subplots(figsize=(10,5))
ax.set_title('Intersection graph')
# pos = nx.circular_layout(F)
# axes[0].set_title('Labelled graph')
# nx.draw(F, pos, with_labels=True, ax = axes[0])
# axes[1].set_title('Nonlabeled graph')
# nx.draw(F, pos, with_labels=False, ax = axes[1])

g_edges = []
with open('data_lines.txt', 'r') as f:
	for i, line in enumerate(f.readlines()):
		g_edges = list(it.chain(g_edges, it.product([i + 1],
		list(map(int,line.strip().split(','))))))	
g_nodes = list(range(-6,9,3))	
G.add_nodes_from(g_nodes)

g_edges = [(x,y) for x in g_nodes for y in g_nodes if (x+y in g_nodes) or
(abs(x-y) in g_nodes)]

labels = {n:n for n,val in G.nodes.items()}
G.add_edges_from(g_edges)

pos = nx.circular_layout(G)
nx.draw_networkx_labels(G, pos, labels, **label_options)
nx.draw(G, pos, **graph_options)
plt.show()
