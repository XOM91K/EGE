def g(s1, s2, p):
    if (s1 >= 50 or s2 >= 50) and (p == 4 or p == 2):
        return 1
    elif not(s1 >= 50 or s2 >= 50) and p == 4:
        return 0
    elif (s1 >= 50 or s2 >= 50) and p < 4:
        return 0
    if p % 2 == 0:
        return g(s1 + 3, s2, p + 1) and g(s1 * 2, s2, p + 1) and g(s1, s2 + 3, p + 1) and g(s1, s2 * 2, p + 1)
    else:
        return g(s1 + 3, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 3, p + 1) or g(s1, s2 * 2, p + 1)
for S in range(28):
    if g(22, S, 0):
        print(S)
#22
#11 21