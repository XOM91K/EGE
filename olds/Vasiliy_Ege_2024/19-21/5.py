def g(s, p):
    if p == 3 and s >= 135:
        return 1
    elif p == 3 and s < 135:
        return 0
    elif p < 3 and s >= 135:
        return 0
    if p % 2 == 0:
        return g(s + 5, p + 1) or g(s * 3, p + 1)
    else:
        return g(s + 5, p + 1) and g(s * 3, p + 1)
for x in range(1, 134):
    if g(x, 0):
        print(x)