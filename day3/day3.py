with open("./input.txt") as f:
    input = f.read()

x = [0, 0]
y = [0, 0]
dx = {'<': -1, '>': 1, '^': 0, 'v': 0}
dy = {'<': 0, '>': 0, '^': 1, 'v': -1}
s = [set(), set()]
s[0].add((x[0], y[0]))
s[1].add((x[1], y[1]))
for idx, c in enumerate(input):
    x[idx % 2] += dx[c]
    y[idx % 2] += dy[c]
    s[idx % 2].add((x[idx % 2], y[idx % 2]))
print(len(s[0] | s[1]))
