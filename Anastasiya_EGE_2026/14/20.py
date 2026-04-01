def v75(d):
    s = []
    while d > 0:
        s.append(d % 75)
        d //= 75
    return s[::-1]
for x in range(1, 32001):
    d = 75 ** 314 + 75 ** 118 - x
    d = v75(d)
    if d.count(0) < 196:
        print(x, d.count(0))