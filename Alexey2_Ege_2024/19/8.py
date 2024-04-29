def g(s, p, flag):
    if s >= 140 and (p == 2 or p == 4):
        return 1
    elif s < 140 and p == 4:
        return 0
    elif s >= 140 and p < 4:
        return 0
    if p % 2 == 0:
        if flag == 0:
            return g(s + 1, p + 1, 1) and g(s + 2, p + 1, 2) and g(s * 3, p + 1, 3)
        if flag == 1:
            return g(s + 2, p + 1, 2) and g(s * 3, p + 1, 3)
        if flag == 2:
            return g(s + 1, p + 1, 1) and g(s * 3, p + 1, 3)
        if flag == 3:
            return g(s + 1, p + 1, 1) and g(s + 2, p + 1, 2)
    else:
        if flag == 0:
            return g(s + 1, p + 1, 1) or g(s + 2, p + 1, 2) or g(s * 3, p + 1, 3)
        if flag == 1:
            return g(s + 2, p + 1, 2) or g(s * 3, p + 1, 3)
        if flag == 2:
            return g(s + 1, p + 1, 1) or g(s * 3, p + 1, 3)
        if flag == 3:
            return g(s + 1, p + 1, 1) or g(s + 2, p + 1, 2)
for x in range(1, 140):
    if g(x, 0, 0):
        print(x)