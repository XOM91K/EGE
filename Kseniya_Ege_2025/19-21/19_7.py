def g(s, p):
    if s <= 1 and p == 2:
        return 1
    if s > 1 and p == 2:
        return 0
    if s <= 1 and p < 2:
        return 0
    if p % 2 == 0:
        if s % 3 == 0 and s < 4:
            return g(s - 1, p + 1) and g(s // 3, p + 1)
        elif s % 3 == 0 and s >= 4:
            return g(s - 1, p + 1) and g(s // 3, p + 1) and g(s - 4, p + 1)
        elif s >= 4:
            return g(s - 1, p + 1) and g(s - 4, p + 1)
        else:
            return g(s - 1, p + 1)
    else:
        if s % 3 == 0 and s < 4:
            return g(s - 1, p + 1) or g(s // 3, p + 1)
        elif s % 3 == 0 and s >= 4:
            return g(s - 1, p + 1) or g(s // 3, p + 1) or g(s - 4, p + 1)
        elif s >= 4:
            return g(s - 1, p + 1) or g(s - 4, p + 1)
        else:
            return g(s - 1, p + 1)


for S in range(4, 100):
    if g(S, 0):
        print(S)
