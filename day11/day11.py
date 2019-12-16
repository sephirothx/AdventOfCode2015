from string import ascii_lowercase as letters
import re

INPUT_1 = "hxbxwxba"
INPUT_2 = "hxbxxyzz"
next_lett = {c: next_c for c, next_c in zip(letters, letters[1:])}


def repl(m):
    return next_lett[m.group(1)] + len(m.group(2)) * "a"


s = INPUT_1
while True:
    s = re.sub(r"(\w)(z*)$", repl, s)
    if ((not any([ord(b) == next_lett.get(a) + 1 and ord(c) == ord(b) + 1 for a, b, c in zip(s, s[1:], s[2:])]))
            or ("i" in s or "o" in s or "l" in s)
            or (len(re.findall(r"(.)\1", s)) < 2)):
        continue
    break

print(s)
