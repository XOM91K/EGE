def g(s1, s2, p):
    if s1 + s2 >= 212 and (p == 4):
        return 1
    elif s1 + s2 < 212 and p == 4:
        return 0
    elif s1 + s2 >= 212 and p < 4:
        return 0
    if p % 2 == 1:
        return g(s1 + s2, s2, p + 1) or g(s1, s1 + s2, p + 1)
    else:
        return g(s1 + s2, s2, p + 1) and g(s1, s1 + s2, p + 1)
for x in range(0, 112):
    if g(10, x, 0):
        print(x)