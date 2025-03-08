def v15(d):
    s = []
    while d > 0:
        s.append(d % 15)
        d //= 15
    return s[::-1]
c = 3 * 15 ** 1140 + 2 * 15 ** 1025 + 15 ** 923 - 3 * 15 ** 85 + 2 * 15 ** 74 + 3
c = v15(c)
print(c)