import re

with open("./input.txt") as f:
    INPUT = f.read().split('\n')

r = re.compile(r'.*: (.*): (\d+), (.*): (\d+), (.*): (\d+)')
req = {"children": 3,
       "cats": 7,
       "samoyeds": 2,
       "pomeranians": 3,
       "akitas": 0,
       "vizslas": 0,
       "goldfish": 5,
       "trees": 3,
       "cars": 2,
       "perfumes": 1}
more = ("cats",  "trees")
less = ("pomeranians", "goldfish")
sue = []
for s in INPUT:
    t1, q1, t2, q2, t3, q3 = r.match(s).groups()
    d = {t1: int(q1), t2: int(q2), t3: int(q3)}
    sue.append(d)

# part 1
for i, s in enumerate(sue):
    done = True
    for c in s:
        done &= s[c] == req[c]
    if done:
        print(i+1)
        break

# part 2
for i, s in enumerate(sue):
    done = True
    for c in s:
        if c in more:
            done &= s[c] > req[c]
        elif c in less:
            done &= s[c] < req[c]
        else:
            done &= s[c] == req[c]
    if done:
        print(i+1)
        break
