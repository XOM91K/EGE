def v11(d):
    s = []
    while d > 0:
        s.append(d % 11)
        d //= 11
    return s
for x in range(1, 100_000):
    d = 11 ** 250 + 11 ** 5 - 358123 - x
    d = v11(d)
    if d.count(10) == 248 and x % 3 == 0:
        print(x)