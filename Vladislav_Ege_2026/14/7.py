def v25(d):
    s = []
    while d > 0:
        s.append(str(d % 25))
        d //= 25
    return s
for x in range(1, 2501):
    d = 25 ** 15 + 25 ** 100 - x
    d = v25(d)
    if d.count('0') > 86:
        print(x, d.count('0'))