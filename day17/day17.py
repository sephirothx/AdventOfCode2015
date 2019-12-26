from itertools import combinations

with open("./input.txt") as f:
    INPUT = [int(s) for s in f.read().split('\n')]

def count_combinations(goal, containers):
    ans = 0
    for i in range(len(containers)):
        s = 0
        for c in combinations(containers, i):
            if sum(c) == goal:
                s += 1
        ans += s
        if s > 0:
            print(i, s)
    return ans

print(count_combinations(150, INPUT))
