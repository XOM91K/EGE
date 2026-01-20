def g(s1, s2, p):
    if s1 + s2 >= 323 and p == 2:
        return 1
    elif s1 + s2 < 323 and p == 2:
        return 0
    elif s1 + s2 >= 323 and p < 2:
        return 0
    if p % 2 == 0:
        return g(s1 + 3, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 3, p + 1) or g(s1, s2 * 2, p + 1)
    else:
        return g(s1 + 3, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 3, p + 1) or g(s1, s2 * 2, p + 1)
for S in range(1, 200):
    if g(123, S, 0):
        print(S)