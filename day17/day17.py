from itertools import combinations

with open("./input.txt") as f:
    INPUT = [int(s) for s in f.read().split('\n')]

def count_combinations(goal, containers):
    ans = 0
    for i in range(len(containers)):
        tot = 0
        for c in combinations(containers, i):
            if sum(c) == goal:
                tot += 1
        ans += tot
        if tot > 0:
            print(i, tot)
    return ans

print(count_combinations(150, INPUT))
