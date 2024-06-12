def g(s1, p, k):
    if s1 >= 140 and (p == 4 or p == 2):
        return True
    elif s1 < 140 and p == 4:
        return False
    elif s1 >= 140:
        return False
    if p % 2 == 0:
        if k == 0:
            return g(s1 + 1, p + 1, 1) and g(s1 + 2, p + 1, 2) and g(s1 * 3, p + 1, 3)
        elif k == 1:
            return g(s1 + 2, p + 1, 2) and g(s1 * 3, p + 1, 3)
        elif k == 2:
            return g(s1 + 1, p + 1, 1) and g(s1 * 3, p + 1, 3)
        elif k == 3:
            return g(s1 + 1, p + 1, 1) and g(s1 + 2, p + 1, 2)
    else:
        if k == 0:
            return g(s1 + 1, p + 1, 1) or g(s1 + 2, p + 1, 2) or g(s1 * 3, p + 1, 3)
        elif k == 1:
            return g(s1 + 2, p + 1, 2) or g(s1 * 3, p + 1, 3)
        elif k == 2:
            return g(s1 + 1, p + 1, 1) or g(s1 * 3, p + 1, 3)
        elif k == 3:
            return g(s1 + 1, p + 1, 1) or g(s1 + 2, p + 1, 2)
for x in range(1, 140):
    if g(x, 0, 0):
        print(x)
#19 - 46
#20 - 16, 45
#21 - 15