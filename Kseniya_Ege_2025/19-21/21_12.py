def g(s1, s2, p):
    if s1 * s2 >= 385 and (p == 2 or p == 4):
        return 1
    if s1 * s2 < 385 and p == 4:
        return 0
    if s1 * s2 >= 385 and p < 4:
        return 0
    if p % 2 == 0:
        return g(s1 + 5, s2, p + 1) and g(s1 * 2, s2, p + 1) and g(s1, s2 + 5, p + 1) and g(s1, s2 * 2, p + 1)
    else:
        return g(s1 + 5, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 5, p + 1) or g(s1, s2 * 2, p + 1)
for S in range(1, 385):
    if g(8, S, 0):
        print(S)