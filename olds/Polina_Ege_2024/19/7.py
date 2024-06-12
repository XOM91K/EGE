def g(s1, s2, p):
    if p == 3 and s1 + s2 >= 231:
        return 1
    elif p == 3 and s1 + s2 < 231:
        return 0
    elif s1 + s2 >= 231:
        return 0
    if p % 2 != 0:
        return g(s1 + 4, s2, p + 1) and g(s1 * 3, s2, p + 1) and g(s1, s2 + 4, p + 1) and g(s1, s2 * 3, p + 1)
    else:
        return g(s1 + 4, s2, p + 1) or g(s1 * 3, s2, p + 1) or g(s1, s2 + 4, p + 1) or g(s1, s2 * 3, p + 1)
for x in range (1,218):
    if g(10,x,0):
        print(x)