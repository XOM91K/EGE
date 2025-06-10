def g(s, p):
    if p == 3 and s >= 67:
        return 1
    elif p == 3 and s < 67:
        return 0
    elif p < 3 and s >= 67:
        return 0
    if p % 2 == 1:
        return g(s + 1, p + 1) and g(s + 3, p + 1) and g(s * 2, p + 1)
    else:
        return g(s + 1, p + 1) or g(s + 3, p + 1) or g(s * 2, p + 1)
for S in range(1, 67):
    if g(S, 0) == 1:
        print(S)