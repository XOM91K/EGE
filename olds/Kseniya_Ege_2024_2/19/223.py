def g(s, p):
    if s >= 30 and p == 3:
        return 1
    elif s < 30 and p == 3:
        return 0
    elif s >= 30 and p < 3:
        return 0
    return g(s + 1, p + 1) or g(s * 2, p + 1)
for S in range(1, 30):
    if g(S, 0):
        print(S)