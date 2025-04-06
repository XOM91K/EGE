def g(s, p):
    if s >= 51 and p == 3:
        return 1
    if s < 51 and p == 3:
        return 0
    if s >= 51 and p < 3:
        return 0
    if p % 2 == 0:
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 2, p + 1)
    else:
        return g(s + 1, p + 1) and g(s + 4, p + 1) and g(s * 2, p + 1)
for S in range(1, 51):
    if g(S, 0):
        print(S)