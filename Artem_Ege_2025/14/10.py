def v11(d):
    s = []
    while d > 0:
        s.append(d % 11)
        d //= 11
    return s[::-1]
for x in range(1, 100000):
    d = 11 ** 250 + 11 ** 5 - 358123 - x
    d = v11(d)
    if x % 3 == 0:
        if d.count(10) == 248:
            print(x)
            break