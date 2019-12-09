a = open("./input.txt")
s = a.read()

ans = s.count('(') - s.count(')')
print(ans)

c = 0
for idx, i in enumerate(s):
    if i == '(':
        c = c + 1
    else:
        c = c - 1
    if c == -1:
        print(idx + 1)
