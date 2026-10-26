def g(s, p):
    if s >= 231 and p == 3:
        return 1
    elif s < 231 and p == 3:
        return 0
    elif s >= 231 and p < 3:
        return 0
    if p % 2 != 0:
        return g(s+5, p+1) and g(s*3, p+1)
    else:
        return g(s+3, p+1) or g(s*3, p+1)
for s in range(10, 121):
    if g(s, 0):
        print(s)