from builtins import min

INPUT = 29000000
i = 1
s = 0
house = [0 for _ in range(1000000)]

def sol():
    for elf in range(1, 1000000):
        for h in range(elf, min(50*elf+1, 1000000), elf):
            house[h] += elf*11
        if house[elf] >= INPUT:
            return elf

print(sol())
