def g(s, p):
    if (p == 4 or p == 2) and s >= 25:
        return 1
    elif p == 4 and s < 25:
        return 0
    elif s >= 25:
        return 0
    if p % 2 == 0:
        return g(s + 2, p + 1) and g(s * 2, p + 1)
    else:
        return g(s + 2, p + 1) or g(s * 2, p + 1)
for x in range(1, 25):
    if g(x, 0):
        print(x)