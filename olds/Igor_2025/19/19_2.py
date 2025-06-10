def g(s1, s2, p):
    if s1 + s2 >= 77 and (p == 2 or p == 4):
        return 1
    elif (s1 + s2 < 77 and p == 4) or (s1 + s2 >= 77):
        return 0
    if p % 2 != 0:
        return g(s1 + 1, s2, p + 1) or g(s1 * 2, s2, p + 1) or g(s1, s2 + 1, p + 1) or g(s1, s2 * 2, p + 1)
    return g(s1 + 1, s2, p + 1) and g(s1 * 2, s2, p + 1) and g(s1, s2 + 1, p + 1) and g(s1, s2 * 2, p + 1)
for S in range(1, 70):
    if g(7, S, 0):
        print(S)
#18
#31 34
#30