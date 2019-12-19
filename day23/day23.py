with open("./input.txt") as f:
    INPUT = f.read().split('\n')

reg = {'a': 1, 'b': 0}
ip = 0
while ip < len(INPUT):
    i = INPUT[ip].replace(',', '').split(' ')
    if i[0] == "hlf":
        reg[i[1]] //= 2
        ip += 1
    elif i[0] == "tpl":
        reg[i[1]] *= 3
        ip += 1
    elif i[0] == "inc":
        reg[i[1]] += 1
        ip += 1
    elif i[0] == "jmp":
        ip += int(i[1])
    elif i[0] == "jie":
        ip += int(i[2]) if reg[i[1]] % 2 == 0 else 1
    elif i[0] == "jio":
        ip += int(i[2]) if reg[i[1]] == 1 else 1

print(reg['b'])
