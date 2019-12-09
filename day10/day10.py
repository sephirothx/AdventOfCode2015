INPUT = "1321131112"

def play(s):
    output = ""
    curr, count = s[0], 1
    for i, c in enumerate(s[1:]):
        if c == curr:
            count += 1
        else:
            output += str(count) + curr
            curr, count = c, 1
    output += str(count) + curr
    return output

for _ in range(50):
    INPUT = play(INPUT)
print(len(INPUT))
