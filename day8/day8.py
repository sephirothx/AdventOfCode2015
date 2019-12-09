import re

with open("./input.txt") as f:
    INPUT = f.read()

s = re.sub(r"\\\"|\\\\|\\x..", "1", INPUT).replace("\"", "")
print(len(INPUT)-len(s))

s = re.sub(r"[\\\"]", "11", INPUT)
print(len(s) + 2*len(s.split('\n')) - len(INPUT))
