def v15(d):
    s = []
    while d > 0:
        s.append(d % 15)
        d //= 15
    return s[::-1]
for x in range(1, 100000):
    d = 15 ** 450 + 15 ** 100 - 11123471 - x
    d = v15(d)
    if x % 11 == 0 and d.count(14) == 97:
        print(x, d)