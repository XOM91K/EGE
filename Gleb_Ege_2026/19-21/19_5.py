def g(s1, s2, p):
    if s1 + s2 >= 212 and p == 1:
        return 1
    elif s1 + s2 < 212 and p == 1:
        return 0
    elif s1 + s2 >= 212 and p < 1:
        return 0

    if p % 2 == 0:
        return g(s1 + s2, s2, p + 1) or g(s1, s2 + s1, p + 1)
    else:
        return g(s1 + s2, s2, p + 1) or g(s1, s2 + s1, p + 1)
for S in range(0, 112):
    if g(100, S, 0) == 0:
        print(S)