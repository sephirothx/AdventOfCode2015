with open("./input.txt") as f:
    INPUT = f.read().split('\n')

d = {}
memo = {}


def calc(w):
    if w in memo:
        return memo[w]

    try:
        return int(w)
    except ValueError:
        pass

    o = d[w]
    r = 0
    if len(o) == 1:
        r = calc(o[0])
    else:
        if o[-2] == "NOT":
            r = ~calc(o[1])
        elif o[-2] == "AND":
            r = calc(o[0]) & calc(o[2])
        elif o[-2] == "OR":
            r = calc(o[0]) | calc(o[2])
        elif o[-2] == "LSHIFT":
            r = calc(o[0]) << calc(o[2])
        elif o[-2] == "RSHIFT":
            r = calc(o[0]) >> calc(o[2])
    memo[w] = r
    return r


for s in INPUT:
    op, res = s.split(' -> ')
    d[res] = op.split(' ')
ans1 = calc('a')
memo = {'b': ans1}
ans2 = calc('a')
print(ans1, ans2)
