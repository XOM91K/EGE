def v3(x):
    k = ''
    while x > 0:
        k += str(x % 3)
        x //= 3
    return k[::-1]

c = []
for x in range(1, 10000):
    r = v3(x)
    if x % 3 == 0:
        r = r + r[-2:]
    else:
        r = r + v3(r.count('2') * 2 + r.count('1'))
    r = int(r, 3)
    if r > 278 and r % 2 != 0:
        c.append(r)
print(min(c))
