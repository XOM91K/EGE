def g(s1, s2, p):
    if s1 + s2 >= 123 and p == 3:
        return 1
    elif s1 + s2 < 123 and p == 3:
        return 0
    elif s1 + s2 >= 123 and p < 3:
        return 0
    if p % 2 == 0:
        return g(s1 + 1, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 1, p + 1) or g(s1, s2 * 2, p + 1)
    else:
        return g(s1 + 1, s2, p + 1) and g(s1 * 2, s2, p + 1) and g(s1, s2 + 1, p + 1) and g(s1, s2 * 2, p + 1)
for s in range(1, 110):
    if g(13, s, 0):
        print(s)
#28
#48 54