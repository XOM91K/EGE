def v25(d):
    s = []
    while d > 0:
        s.append(d % 25)
        d //= 25
    return s[::-1]
for x in range(1, 2501):
    d = 25 ** 150 + 25 ** 100 - x
    d = v25(d)
    if d.count(0) > 51:
        print(x, d.count(0))