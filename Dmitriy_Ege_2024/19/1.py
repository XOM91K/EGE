def g(s, p):
    if s >= 88 and p == 2:
        return 1
    elif s < 88 and p == 2:
        return 0
    elif s >= 88:
        return 0
    if p % 2 == 0:
        return g(s + 1, p + 1) and g(s + 4, p + 1) and g(s * 3, p + 1)
    else:
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 3, p + 1)
for x in range(1, 88):
    if g(x, 0):
        print(x)