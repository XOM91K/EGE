def g(s, p):
    if (p == 4 or p == 2) and s >= 108:
        return 1
    elif p == 4 and s < 108:
        return 0
    elif p < 4 and s >= 108:
        return 0
    if p % 2 == 0:
        return g(s + 1, p + 1) and g(s * 2 if s % 2 != 0 else s * 1.5, p + 1)
    else:
        return g(s + 1, p + 1) or g(s * 2 if s % 2 != 0 else s * 1.5, p + 1)
for S in range(1, 108):
    if g(S, 0):
        print(S)