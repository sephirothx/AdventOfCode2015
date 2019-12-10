import json

with open("./input.txt") as f:
    INPUT = f.read()

def calc(j):
    if type(j) == int:
        return j
    if type(j) == list:
        return sum([calc(jj) for jj in j])
    if type(j) == dict:
        if 'red' in j.values():
            return 0
        return calc(list(j.values()))
    return 0

ans = calc(json.loads(INPUT))
print(ans)
