def g(s, p):
    if s >= 108 and (p == 2 or p == 4):
        return 1
    elif s < 108 and p == 4:
        return 0
    elif s >= 108 and p < 4:
        return 0

    if p % 2 == 0:
        return g(s + 1, p + 1) and g(s * 2 if s % 2 != 0 else s * 1.5, p + 1)
    else:
        return g(s + 1, p + 1) or g(s * 2 if s % 2 != 0 else s * 1.5, p + 1)
for S in range(1, 108):
    if g(S, 0):
        print(S)