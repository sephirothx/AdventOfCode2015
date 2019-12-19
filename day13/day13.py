import re
from copy import deepcopy
from itertools import permutations

import networkx as nx

with open("./input.txt") as f:
    INPUT = f.read().split('\n')

g = nx.DiGraph()

for s in INPUT:
    p1, v, h, p2 = re.match(r'(\w+).*?(\w+) (\d+).*?(\w+)\.', s).groups()
    g.add_edge(p1, p2, happiness=int(h) if v == "gain" else -int(h))

nodes = deepcopy(g.nodes())
for n in nodes:
    g.add_edge("me", n, happiness=0)
    g.add_edge(n, "me", happiness=0)

max_h = 0
for p in permutations(g.nodes()):
    dh = 0
    for a, b in zip(p, p[1:]+p[:1]):
        dh += g[a][b]["happiness"] + g[b][a]["happiness"]
    max_h = max(max_h, dh)

print(max_h)
