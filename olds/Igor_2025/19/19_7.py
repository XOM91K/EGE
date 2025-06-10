def g(s, p):
    if s <= 19 and p == 2:
        return 1
    if s > 19 and p == 2:
        return 0
    if s <= 19 and p < 2:
        return 0
    if p % 2 == 0:
        if s % 2 == 0 and s % 3 == 0:
            return g(s - 5, p + 1) and g(s // 2, p + 1) and g(s // 3, p + 1)
        elif s % 2 == 0:
            return g(s - 5, p + 1) and g(s // 2, p + 1)
        elif s % 3 == 0:
            return g(s - 5, p + 1) and g(s // 3, p + 1)
        else:
            return g(s - 5, p + 1) and g(s + 1, p + 1)
    else:
        if s % 2 == 0 or s % 3 == 0:
            return g(s - 5, p + 1) or g(s // 2, p + 1) or g(s // 3, p + 1)
        elif s % 2 == 0:
            return g(s - 5, p + 1) or g(s // 2, p + 1)
        elif s % 3 == 0:
            return g(s - 5, p + 1) or g(s // 3, p + 1)
        else:
            return g(s - 5, p + 1) or g(s + 1, p + 1)
for S in range(20, 1000):
    if g(S, 0):
        print(S)
#25