import re

with open("./input.txt") as f:
    INPUT = f.read()

m = re.findall(r"-?\d+", INPUT)
ans = sum(map(int, m))
print(ans)
