def g(s, p):
    if s >= 58 and (p == 2 or p == 4):
        return 1
    if s < 58 and p == 4:
        return 0
    if s >= 58 and p < 4:
        return 0
    if p % 2 == 0:
        return g(s + 1, p + 1) and g(s + 4, p + 1) and g(s * 2, p + 1)
    else:
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 2, p + 1)
for x in range(1, 57):
    if g(x, 0):
        print(x)