def g(s, p):
    if s >= 84 and p == 3:
        return 1
    elif s < 84 and p == 3:
        return 0
    elif s >= 84 and p < 3:
        return 0
    if p % 2 == 0:
        return g(s + 1, p + 1) or g(s * 1.5 if s % 2 == 0 else s * 2, p + 1)
    else:
        return g(s + 1, p + 1) and g(s * 1.5 if s % 2 == 0 else s * 2, p + 1)
for S in range(1, 84):
    if g(S, 0):
        print(S)