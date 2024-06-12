def g(s1, s2, p):
    if (p == 4 or p == 2) and s1 + s2 >= 99:
        return 1
    elif p == 4 and s1 + s2 < 99:
        return 0
    elif s1 + s2 >= 99:
        return 0
    if p % 2 != 0:
        return g(s1 + 1, s2, p + 1) or g(s1 * 3, s2, p + 1) or g(s1, s2 + 1, p + 1) or g(s1, s2 * 3, p + 1)
    else:
        return g(s1 + 1, s2, p + 1) and g(s1 * 3, s2, p + 1) and g(s1, s2 + 1, p + 1) and g(s1, s2 * 3, p + 1)
for x in range(1, 91):
    if g(8, x, 0):
        print(x)