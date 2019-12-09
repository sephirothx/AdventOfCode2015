import networkx.algorithms
from itertools import permutations

with open("./input.txt") as f:
    INPUT = f.read().split('\n')

g = networkx.Graph()
for s in INPUT:
    a = s.split(' ')
    g.add_edge(a[0], a[2], dist=int(a[4]))

ans1, ans2 = 10000, 0
for p in permutations(g.nodes()):
    d = 0
    for i, n in enumerate(p[1:]):
        d += g[n][p[i-1]]["dist"]
    ans1 = min(ans1, d)
    ans2 = max(ans2, d)

print(ans1, ans2)
