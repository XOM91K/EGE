def g(s1, s2, p):
    if s1 + s2 >= 83 and (p == 2 or p == 4):
        return 1
    elif s1 + s2 < 83 and p == 4:
        return 0
    elif s1 + s2 >= 83 and p < 4:
        return 0
    if p % 2 == 0:
        return g(s1 + 1, s2, p + 1) and g(s1 * 4, s2, p + 1) and g(s1, s2 + 1, p + 1) and g(s1, s2 * 4, p + 1)
    else:
        return g(s1 + 1, s2, p + 1) or g(s1 * 4, s2, p + 1) or g(s1, s2 + 1, p + 1) or g(s1, s2 * 4, p + 1)
for s in range(1, 78):
    if g(5, s, 0):
        print(s)
#3
#2 19
#18
