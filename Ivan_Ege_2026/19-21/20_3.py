def g(s, p):
    if s >= 56 and p == 3:
        return 1
    elif s <  56 and p == 3:
        return 0
    elif s >= 56 and p < 3:
        return 0
    if p%2!=0:
        if s % 3 == 0:
            return g(s+1, p+1) and g(s+2, p+1) and g(s*3, p+1)
        else:
            return g(s + 1, p + 1) and g(s + 2, p + 1)
    else:
        if s % 3 == 0:
            return g(s + 1, p + 1) or g(s + 2, p + 1) or g(s * 3, p + 1)
        else:
            return g(s + 1, p + 1) or g(s + 2, p + 1)

for s in range(1, 56):
    if g(s, 0):
        print(s)