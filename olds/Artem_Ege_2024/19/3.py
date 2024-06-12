def g(s1, s2, p):
    if s1 + s2 >= 90 and (p == 2 or p == 4):
        return 1
    elif s1 + s2 < 90 and p == 4:
        return 0
    elif s1 + s2 >= 90 and p < 4:
        return 0
    if p % 2 == 0:
        return g(s1 + 1, s2, p + 1) and g(s1, s2 + 1, p + 1) and g(s1 * 3, s2, p + 1) and g(s1, s2 * 3, p + 1)
    else:
        return g(s1 + 1, s2, p + 1) or g(s1, s2 + 1, p + 1) or g(s1 * 3, s2, p + 1) or g(s1, s2 * 3, p + 1)
for x in range(1, 81):
    if g(9, x, 0) == 1:
        print(x)
#9
#1
#
