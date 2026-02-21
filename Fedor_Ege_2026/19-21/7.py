def g(s, p):
    if s <= 1 and p == 2:
        return 1
    if s > 1 and p == 2:
        return 0
    if s <= 1 and p < 2:
        return 0
    if p % 2 == 0:
        if s >= 4 and s % 3 == 0:
            return g(s - 1, p + 2) and g(s - 4, p + 1) and g(s // 3, p + 1)
        elif s < 4 and s % 3 == 0:
            return g(s - 1, p + 2) and g(s // 3, p + 1)
        elif s >= 4 and s % 3 != 0:
            return g(s - 1, p + 2) and g(s - 4, p + 1)
        else:
            return g(s - 1, p + 2)
    else:
        if s >= 4 and s % 3 == 0:
            return g(s - 1, p + 2) or g(s - 4, p + 1) or g(s // 3, p + 1)
        elif s < 4 and s % 3 == 0:
            return g(s - 1, p + 2) or g(s // 3, p + 1)
        elif s >= 4 and s % 3 != 0:
            return g(s - 1, p + 2) or g(s - 4, p + 1)
        else:
            return g(s - 1, p + 2)


for s1 in range(4, 101):
    if g(s1, 0):
        print(s1)
