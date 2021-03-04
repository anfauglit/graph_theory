import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import string

committes = []
with open('data.txt', 'r') as f:
	for line in f.readlines():
		committes.append(line.strip().split(','))

committes_flat = list(np.concatenate(committes).flat)
committe_members = np.unique(committes_flat)
committes = list(map(set, committes))

committes_with_commons = []
for i, c in enumerate(committes):
	for j, d in enumerate(committes[i + 1:]):
		if len(c & d) > 0:
			committes_with_commons.append((i, i + j + 1))

			
G = nx.Graph()

G.add_nodes_from(range(len(committes)))
labels = dict([(x, x + 1) for x in range(len(committes))])

G.add_edges_from(committes_with_commons)

H = nx.Graph()
H.add_nodes_from([2,3,5,8,13,21])
fibo_edges = []

for n in H.nodes:
	for m in H.nodes:
		if (n + m in H.nodes) or (abs(n - m) in H.nodes):
			if (m, n) not in fibo_edges:
				fibo_edges.append((n,m))

H.add_edges_from(fibo_edges)

graph_options = {
	'with_labels': False,
	'node_color': 'k',
	'edge_color': 'r',
}

label_options = {
	'font_color': 'w',
	'font_size': 10,
}

# nx.draw(H, with_labels=True)
pos = nx.circular_layout(G)
# nx.draw_networkx_labels(G, pos, labels, **label_options) 
# nx.draw(G, pos, **graph_options)

F = nx.Graph()
raw_edges_f = 'uv uw vw vx wx xy'
f_nodes = set(raw_edges_f)
f_nodes.remove(' ')
f_nodes = list(f_nodes)

F.add_nodes_from(f_nodes)

f_edges = []
for edge in raw_edges_f.split(' '):
	f_edges.append(tuple(edge))
F.add_edges_from(f_edges)

fig, ax = plt.subplots(figsize=(10,5))
# pos = nx.circular_layout(F)
# axes[0].set_title('Labelled graph')
# nx.draw(F, pos, with_labels=True, ax = axes[0])
# axes[1].set_title('Nonlabeled graph')
# nx.draw(F, pos, with_labels=False, ax = axes[1])

E = nx.Graph()
e_edges = []
e_nodes = []
with open('data_coins.txt', 'r') as f:
	for i, line in enumerate(f.readlines()):
		e_nodes.append(i + 1)
		for node in line.strip().split(','):
			e_edges.append((i + 1, int(node)))

E.add_nodes_from(e_nodes)
E.add_edges_from(e_edges)
pos = nx.circular_layout(E)
# nx.draw(E, pos, with_labels=True)

K = nx.Graph()
with open('data_words.txt', 'r') as f:
	words = f.readline().strip().split(', ')

k_edges = []

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

for word1 in words:
	for word2 in words[words.index(word1) + 1:]:
		if comp_words(word1, word2):
			k_edges.append((word1, word2))

K.add_nodes_from(words)
K.add_edges_from(k_edges)
labels = {n:n for n in K.nodes}
pos = nx.spring_layout(K)

max_x = max([x for x,y in pos.values()])
min_x = min([x for x,y in pos.values()])
space = abs(max_x - min_x)
ax.set_xlim(min_x * 1.2, max_x * 1.2)

xlabel_offset = 0.05 * space
new_pos = {}
for k,v in pos.items():
	new_pos[k] = (v[0] + xlabel_offset, v[1])

nx.draw_networkx_labels(K, new_pos, labels, font_size=10)
nx.draw(K, pos, **graph_options)
plt.show()
