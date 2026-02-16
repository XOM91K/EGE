def v25(d):
    s = []
    while d > 0:
        s.append(str(d % 25))
        d //= 25
    return s
c = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 5 * 25 ** 4 - 2025
c = v25(c)
print(c.count('0'))