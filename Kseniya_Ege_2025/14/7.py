def v15(d):
    s = []
    while d > 0:
        s.append(d % 15)
        d //= 15
    return s
d = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
d = v15(d)
print(set(d))