def g(s, p):
    if (p == 2 or p == 4) and s >= 111:
        return 1
    elif p == 4 and s < 111:
        return 0
    elif p < 4 and s >= 111:
        return 0
    if p % 2 == 0:
        return g(s + 1, p + 1) and g(s + 3, p + 1) and g(s * 4, p + 1)
    else:
        return g(s + 1, p + 1) or g(s + 3, p + 1) or g(s * 4, p + 1)
for x in range(1, 111):
    if g(x, 0):
        print(x)

#27
#24 26
#