import hashlib

INPUT = "yzbqklnj"

i = 1
done = False
while not done:
    h = hashlib.md5()
    h.update(f"{INPUT}{i}".encode('utf-8'))
    d = h.hexdigest()
    if d.startswith("000000"):
        print(i)
        break
    i += 1
