def g(s, p):
    if (p == 2 or p == 4) and s >= 129:
        return True
    if p == 4 and s < 129:
        return False
    if p < 4 and s >= 129:
        return False
    if p % 2 == 0:
        return g(s + 1, p + 1) and g(s * 2, p + 1)
    else:
        return g(s + 1, p + 1) or g(s * 2, p + 1)
for x in range(1, 129):
    if g(x, 0):
        print(x)