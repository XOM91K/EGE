def g(s1, s2, p):
    if s1 * s2 >= 123 and p == 3:
        return 1
    elif s1 * s2 < 123 and p == 3:
        return 0
    elif s1 * s2 >= 123 and p < 3:
        return 0
    if p % 2 == 0:
        return g(s1 + 2, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 2, p + 1) or g(s1, s2 * 2, p + 1)
    else:
        return g(s1 + 2, s2, p + 1) and g(s1 * 2, s2, p + 1) and g(s1, s2 + 2, p + 1) and g(s1, s2 * 2, p + 1)
for S in range(1, 41):
    if g(3, S, 0):
        print(S)
# 17 18