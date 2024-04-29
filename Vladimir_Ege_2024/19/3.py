def g(s, p):
    if s >= 165 and (p == 2 or p == 4):
        return 1
    elif s < 165 and p == 4:
        return 0
    elif s >= 165 and p < 4:
        return 0
    if p % 2 == 0:
        return g(s + 1, p + 1) and g(s * 2, p + 1)
    else:
        return g(s + 1, p + 1) or g(s * 2, p + 1)
for S in range(1, 165):
    if g(S, 0):
        print(S)
#82
#41 81
#80