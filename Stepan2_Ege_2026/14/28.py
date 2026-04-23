def v27(d):
    s = []
    while d > 0:
        s.append(d % 27)
        d //= 27
    return s
for x in range(1, 27000):
    d = 3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3 - x
    d = v27(d)
    if d.count(0) > 7:
        print(x)