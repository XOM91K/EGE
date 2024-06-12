def g(k, i):
    if k >= 301 and i == 3:
        return True
    if k < 301 and i == 3:
        return False
    if k >= 301 and i < 3:
        return False
    if i % 2 == 1:
        return g(k + 3, i + 1) and g(k * 5, i + 1)
    else:
        return g(k + 3, i + 1) or g(k * 5, i + 1)
for s in range(1, 300):
    if g(s, 0):
        print(s)