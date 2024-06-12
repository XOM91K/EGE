def g(s, p):
    if (p == 1 or p == 3 or p == 5) and s >= 21:
        return 1
    elif p == 5 and s < 21:
        return 0
    elif p < 5 and s >= 21:
        return 0
    if p % 2 == 0:
        return g(s + 1, p + 1) or g(s * 2, p + 1)
    else:
        return g(s + 1, p + 1) and g(s * 2, p + 1)
for x in range(1, 21):
    if g(x, 0):
        print(x)