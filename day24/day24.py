from itertools import combinations
from functools import reduce

with open("./input.txt") as f:
    INPUT = [int(s) for s in f.read().split('\n')]

def sol(packages, groups):
    for i in range(len(packages)):
        for c in combinations(packages, i):
            if sum(packages) == groups * sum(c):
                return reduce(lambda x, y: x*y, c, 1)

print(sol(INPUT, 3))
print(sol(INPUT, 4))
