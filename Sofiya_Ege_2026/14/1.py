def v25(d):
    s = ''
    while d > 0:
        s = str(d % 25) + s
        d //= 25
    return s
d = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 5 * 25 ** 4 - 2025
d = v25(d)
print(d.count('0'))