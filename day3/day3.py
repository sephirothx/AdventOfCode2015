with open("./input.txt") as f:
    input = f.read()

x = [0, 0]
y = [0, 0]
dx = {'<': -1, '>': 1, '^': 0, 'v': 0}
dy = {'<': 0, '>': 0, '^': 1, 'v': -1}
s = [set(), set()]
s[0].add((x[0], y[0]))
s[1].add((x[1], y[1]))
for i, c in enumerate(input):
    x[i % 2] += dx[c]
    y[i % 2] += dy[c]
    s[i % 2].add((x[i % 2], y[i % 2]))
print(len(s[0] | s[1]))
