def g(s, p):
    if s >= 313 and p == 2:
        return 1
    if s < 313 and p == 2:
        return 0
    if s >= 313 and p < 2:
        return 0
    if p % 2 == 0:
        return g(s + 2, p + 1) and g(s + 3, p + 1) and g(s * 3, p + 1)
    else:
        return g(s + 2, p + 1) or g(s + 3, p + 1) or g(s * 3, p + 1)
for S in range(1, 313):
    if g(S, 0) == 1:
        print(S)