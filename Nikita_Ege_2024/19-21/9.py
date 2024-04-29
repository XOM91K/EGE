def g(s, p):
    if s >= 100 and p == 3:
        return 1
    elif s < 100 and p == 3:
        return 0
    elif s >= 100 and p < 3:
        return 0
    if p % 2 == 0:
        if p == 0:
            return g(s * 2, p + 1) or g(s + 7, p + 1)
        if p == 2:
            return g(s + 7, p + 1)
    else:
        return g(s + 7, p + 1)
for x in range(1, 100):
    if g(x, 0):
        print(x)