import re

with open("./input.txt") as f:
    INPUT = f.read().split('\n')

ans = 0
for s in INPUT:
    rule1 = len(re.findall(r"(..).*\1", s))
    rule2 = len(re.findall(r"(.).\1", s))
    if rule1 > 0 and rule2 > 0 == 0:
        ans += 1
print(ans)
