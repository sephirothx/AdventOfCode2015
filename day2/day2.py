from functools import reduce

with open("./input.txt") as f:
    s = f.read().split("\n")

print(s)
ans = 0
for p in s:
    sides = tuple(map(int, p.split('x')))
    ribbon = (sum(sides) - max(sides)) * 2 + reduce(lambda x, y: x * y, sides)
    ans += ribbon
print(ans)
