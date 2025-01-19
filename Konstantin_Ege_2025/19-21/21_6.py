def g(s, p):
    if s >= 132 and (p == 2 or p == 4):
        return 1
    if s < 132 and p == 4:
        return 0
    if s >= 132 and p < 4:
        return 0
    if p % 2 == 0:
        return g(s + 3, p + 1) and g(s + 6, p + 1) and g(s * 3, p + 1)
    else:
        return g(s + 3, p + 1) or g(s + 6, p + 1) or g(s * 3, p + 1)
for S in range(1, 132):
    if g(S, 0):
        print(S)