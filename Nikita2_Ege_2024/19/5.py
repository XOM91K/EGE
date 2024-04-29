def g(s1, s2, p):
    if (p == 2 or p == 4) and (s1 + s2) / 2 >= 144:
        return 1
    elif (p == 4) and (s1 + s2) / 2 < 144:
        return 0
    elif p < 4 and (s1 + s2) / 2 >= 144:
        return 0
    if p % 2 == 0:
        return g(s1 + 2, s2, p + 1) and g(s1 * 3, s2, p + 1) and g(s1 +6 , s2 , p + 1) and g(s1, s2 * 3, p + 1) and g(s1, s2 + 2, p + 1) and  g(s1, s2 + 6, p + 1)
    else:
        return g(s1 + 2, s2, p + 1) or g(s1 * 3, s2, p + 1) or g(s1 + 6, s2, p + 1) or g(s1, s2 * 3, p + 1) or g(s1, s2 + 2, p + 1) or  g(s1, s2 + 6, p + 1)
for S in range(1, 105):
    if g(12, S, 0):
        print(S)