import re

with open("./input.txt") as f:
    INPUT = f.read().split('\n')

b = []
for s in INPUT:
    c, d, f, t, cal = map(int, re.match(r'.*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)', s).groups())
    b.append((c, d, f, t, cal))

score = 0
tot = [0]*5
for i in range(100+1):
    for j in range(100+1-i):
        for k in range(100+1-i-j):
            l = 100-k-j-i
            curr = 1
            for t in range(4):
                tot[t] = b[0][t]*i + b[1][t]*j + b[2][t]*k + b[3][t]*l
                curr *= tot[t] if tot[t] > 0 else 0
            calories = b[0][4]*i + b[1][4]*j + b[2][4]*k + b[3][4]*l
            if calories == 500:
                score = max(score, curr)

print(score)
