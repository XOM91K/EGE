def g(s, p):
    if s >= 30 and p == 4:
        return True
    elif s <= 30 and p == 4:
        return False
    elif s >= 30:
        return False
    if p % 3 == 1 or p % 3 == 0:
        return g(s * 2, p + 1) or g(s + 1, p + 1)
    else:
        return g(s * 2, p + 1) and g(s + 1, p + 1)
for i in range(1, 29):
    if g(i, 0):
        print(i)