def g(s, p):
    if p == 2 and s >= 435:
        return 1
    elif p == 2 and s < 435:
        return 0
    elif p < 2 and s >= 435:
        return 0
    if p % 2 == 0:
        return g(s + 5, p + 1) and g(s * 3, p + 1)
    else:
        return g(s + 5, p + 1) or g(s * 3, p + 1)
for s in range(1, 435):
    if g(s, 0):
        print(s)
#140