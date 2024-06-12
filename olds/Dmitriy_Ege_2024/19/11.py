def g(p, s1, s2):
    if (p == 4) and s1 + s2 >= 212:
        return 1
    elif p == 4 and s1 + s2 < 212:
        return 0
    elif p < 4 and s1 + s2 >= 212:
        return 0
    if p % 2 == 0:
        return g(p + 1, s1 + s2, s2) and g(p + 1, s1, s2 + s1)
    else:
        return g(p + 1, s1 + s2, s2) or g(p + 1, s1, s2 + s1)
for S in range(112):
    if g(0,10, S):
        print(S)