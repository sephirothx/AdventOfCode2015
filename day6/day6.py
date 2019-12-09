import re

with open("./input.txt") as f:
    INPUT = f.read().split('\n')

w, h = 1000, 1000
grid = [[0 for x in range(w)] for y in range(h)]

for s in INPUT:
    regex = re.compile(r"(.*) (\d+),(\d+) through (\d+),(\d+)")
    com, x1, y1, x2, y2 = regex.match(s).groups()
    for x in range(int(x1), int(x2)+1):
        for y in range(int(y1), int(y2)+1):
            if com == "turn on":
                grid[x][y] += 1
            elif com == "turn off":
                grid[x][y] -= 1 if grid[x][y] > 0 else 0
            else:
                grid[x][y] += 2
ans = 0
for row in grid:
    for b in row:
        if b:
            ans += b
print(ans)
