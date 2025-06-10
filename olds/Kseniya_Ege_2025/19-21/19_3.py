def g(s, p):
    if s >= 82 and p == 2:
        return 1
    if s < 82 and p == 2:
        return 0
    if s >= 82 and p < 2:
        return 0
    if p % 2 == 0:
        return g(s + 2, p + 1) or g(s + 4, p + 1) or g(s * 3, p + 1)
    else:
        return g(s + 2, p + 1) or g(s + 4, p + 1) or g(s * 3, p + 1)
for x in range(1, 82):
    if g(x, 0):
        print(x)