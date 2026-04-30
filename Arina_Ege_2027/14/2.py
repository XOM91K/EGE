def v27(d):
    l = []
    while d > 0:
        l.append((d % 27))
        d //= 27
    return l[::-1]
d = 2 * 729 ** 75 + 2 * 243 ** 78 + 81 ** 81 + 2 * 27 ** 84 + 2 * 9 ** 87 + 58
d = v27(d)
print(d.count(0))
print(d)
# 150