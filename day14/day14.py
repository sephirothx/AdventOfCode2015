import re

with open("./input.txt") as f:
    INPUT = f.read().split('\n')

r = re.compile(r'.*?(\d+).*?(\d+).*?(\d+).*')
deer = [[int(x) for x in r.match(s).groups()] for s in INPUT]
dist = [0 for x in deer]
points = [0 for x in deer]

for s in range(2503):
    for i, d in enumerate(deer):
        dist[i] += d[0] if (s % (d[1]+d[2])) < d[1] else 0
    m = max(dist)
    for i in [idx for idx, d in enumerate(dist) if d == m]:
        points[i] += 1

print(max(dist))
print(max(points))
