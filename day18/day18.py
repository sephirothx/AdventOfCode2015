with open("./input.txt") as f:
    INPUT = f.read().split('\n')

m = [[c == '#' for c in s] for s in INPUT]

def get_neighbors(x, y):
    return [(x1, y1) for x1 in range(x-1, x+2) for y1 in range(y-1, y+2)
            if 0 <= x1 < len(m) and 0 <= y1 < len(m) and (x, y) != (x1, y1)]

def is_corner(x, y):
    return (x == 0 or x == len(m)-1) and (y == 0 or y == len(m)-1)

for _ in range(100):
    tmp = [[False for _ in range(len(m))] for _ in range(len(m))]
    for y, r in enumerate(m):
        for x, c in enumerate(r):
            n = [m[y1][x1] for x1, y1 in get_neighbors(x, y)].count(True)
            tmp[y][x] = is_corner(x, y) or (m[y][x] and 2 <= n <= 3) or (not m[y][x] and n == 3)
    m = tmp
print([c for r in m for c in r].count(True))