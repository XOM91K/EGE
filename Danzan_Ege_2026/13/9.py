def v27(d):
    s = []
    while d > 0:
        s.append(d % 27)
        d //= 27
    return s[::-1]
for x in range(1, 27001):
    d = 3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3 - x
    d = v27(d)
    if d.count(0) == 6:
        print(x)