def g(s1, s2, p):
    if (p == 2 or p == 4) and s1 + s2 >= 75:
        return 1
    elif p == 4 and s1 + s2 < 75:
        return 0
    elif s1 + s2 >= 75:
        return 0
    if p % 2 != 0:
        return g(s1 + 2, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 2, p + 1) or g(s1, s2 * 2, p + 1)
    else:
        return g(s1 + 2, s2, p + 1) and g(s1 * 2, s2, p + 1) and g(s1, s2 + 2, p + 1) and g(s1, s2 * 2, p + 1)
for x in range(1, 66):
    if g(9, x, 0):
        print(x)
#17
#16