def v13(d):
    s = []
    while d > 0:
        s.append(d % 13)
        d //= 13
    return s[::-1]
for x in range(1, 2000):
    d = 12 * 13 ** 12 + 11 * 13 ** 7 - x
    d = v13(d)
    if d.count(0) % 2 != 0:
        print(x)