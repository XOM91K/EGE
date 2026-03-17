def v13(d):
    s = []
    while d > 0:
        s.append(str(d % 13))
        d //= 13
    return s
for x in range(1, 2000):
    c = 12 * 13 ** 12 + 11 * 13 ** 7 - x
    c = v13(c)
    if c.count('0') % 2 != 0:
        print(x)
