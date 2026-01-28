def v27(d):
    s = []
    while d > 0:
        s.append(d % 27)
        d //= 27
    return s

d = 5 * 729 ** 2024 + 3 * 243 ** 1413 - 7 * 81 ** 169 - 2 * 9 ** 107 + 3017
d = v27(d)

print(d)
#print(d.count(2) * 2 + d.count(4) * 4........)