def g( s, p ):
    if s <= 12 and p == 3:
        return 1
    if s > 12 and p == 3:
        return 0
    if s <= 12 and p < 3:
        return 0
    if p % 2 == 0:
        if s % 2 == 0:
            return g(s - 1, p + 1) or g(s // 2, p + 1)
        else:
            return g(s - 1, p + 1)
    else:
        if s % 2 == 0:
            return g(s - 1, p + 1) and g(s // 2, p + 1)
        else:
            return g(s - 1, p + 1)
for S in range(13, 1000):
    if g(S, 0):
        print(S)