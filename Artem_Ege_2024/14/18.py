def g(d):
    s = []
    while d > 0:
        s.append(d % 25)
        d //= 25
    return s[::-1]
d = 3 * 3125 ** 9 + 2 * 625 ** 8 - 4 * 625 ** 7 + 3 * 125 ** 6 - 2 * 25 ** 5 - 2024
print(g(d).count(0))