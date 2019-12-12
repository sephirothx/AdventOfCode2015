import re
from random import shuffle

with open('./input.txt') as p:
    INPUT = p.read().split('\n\n')

d = []
mol = INPUT[1]
seen = set()
for s in INPUT[0].split('\n'):
    p, r = s.split(" => ")
    d.append((p, r))

# part 1
for p, r in d:
    seen = seen | set([mol[:m.start()] + r + mol[m.end():] for m in re.finditer(p, mol)])
print(len(seen))

# part 2
med = mol
ans = 0
while med != 'e':
    tmp = med
    for r, p in d:
        if p in med:
            med = med.replace(p, r, 1)
            ans += 1
    if tmp == med:
        med = mol
        ans = 0
        shuffle(d)
print(ans)
