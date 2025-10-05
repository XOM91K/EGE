def v25(d):
    k = []
    while d > 0:
        k.append(d % 25)
        d //= 25
    return k[::-1]
d = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 5 * 25 ** 4 - 2025
d = v25(d)
print(d.count(0))