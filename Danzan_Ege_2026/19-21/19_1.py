def g(s, p):
    if s >= 68 and p == 2:
        return 1
    elif s < 68 and p == 2:
        return 0
    elif s >= 68 and p < 2:
        return 0

    if p % 2 == 0:
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 5, p + 1)
    else:
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 5, p + 1)
for S in range(1, 68):
    if g(S, 0) == 1:
        print(S)