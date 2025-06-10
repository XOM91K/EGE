def g(s, p):
    if s < 32 and p == 2:
        return 1
    if s >= 32 and p == 2:
        return 0
    if s < 32 and p < 2:
        return 0

    if p % 2 == 0:
        if s % 4 == 0:
            return g(s - 3, p + 1) and g(s - 2, p + 1) and g(s // 4, p + 1)
        return g(s - 3, p + 1) and g(s - 2, p + 1)
    else:
        if s % 4 == 0:
            return g(s - 3, p + 1) or g(s - 2, p + 1) or g(s // 4, p + 1)
        return g(s - 3, p + 1) or g(s - 2, p + 1)
for S in range(32, 100):
    if g(S, 0):
        print(S)