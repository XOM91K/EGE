def g(s, p):
    if (p == 2 or p == 4) and s >= 68:
        return 1
    elif p == 4 and s < 68:
        return 0
    elif p < 4 and s >= 68:
        return 0
    if p % 2 != 0:
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 5, p + 1)
    else:
        return g(s + 1, p + 1) and g(s + 4, p + 1) and g(s * 5, p + 1)
for S in range(1, 68):
    if g(S, 0) == 1:
        print(S)