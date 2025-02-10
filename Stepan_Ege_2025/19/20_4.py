def g(s1, s2, p):
    if s1 + s2 >= 77 and p == 3:
        return 1
    if s1 + s2 < 77 and p == 3:
        return 0
    if s1 + s2 >= 77 and p < 3:
        return 0
    if p % 2 == 0:
        return g(s1 + 3, s2, p + 1) or g(s1 * 3, s2, p + 1) or g(s1, s2 + 3, p + 1) or g(s1, s2 * 3, p + 1)
    else:
        return g(s1 + 3, s2, p + 1) and g(s1 * 3, s2, p + 1) and g(s1, s2 + 3, p + 1) and g(s1, s2 * 3, p + 1)
for S in range(1, 65):
    if g(12, S, 0):
        print(S)