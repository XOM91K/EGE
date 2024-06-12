def g(s1, s2, p):
    if (s1 > 59 or s2 > 59) and (p == 2 or p == 4):
        return 1
    elif not(s1 > 59 or s2 > 59) and p == 4:
        return 0
    elif (s1 > 59 or s2 > 59) and p < 4:
        return 0
    if p % 2 != 0:
        return g(s1 + 5, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 5, p + 1) or g(s1, s2 * 2, p + 1)
    else:
        return g(s1 + 5, s2, p + 1) and g(s1 * 2, s2, p + 1) and g(s1, s2 + 5, p + 1) and g(s1, s2 * 2, p + 1)
for s in range(1, 59):
    if g(25, s, 0):
        print(s)