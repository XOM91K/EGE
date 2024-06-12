def g(s1, s2, p):
    if s1 + s2 >= 45 and p == 2:
        return True
    elif s1 + s2 < 45 and p == 2:
        return False
    elif s1 + s2 >= 45:
        return False
    if p % 2 == 0:
        return g(s1 + 1, s2, p + 1) or g(s1, s2 + 1, p + 1) or g(s1 * 3, s2, p + 1) or g(s1, s2 * 3, p + 1)
    else:
        return g(s1 + 1, s2, p + 1) or g(s1, s2 + 1, p + 1) or g(s1 * 3, s2, p + 1) or g(s1, s2 * 3, p + 1)
for x in range(1, 41):
    if g(4, x, 0):
        print(x)