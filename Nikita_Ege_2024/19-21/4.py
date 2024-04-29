def g(s1, s2, p):
    if s1 + s2 >= 73 and (p == 4 or p == 2):
        return True
    elif s1 + s2 < 73 and p == 4:
        return False
    elif s1 + s2 >= 73:
        return False
    if p % 2 == 0:
        return g(s1 + 1, s2, p + 1) and g(s1, s2 + 1, p + 1) and g(s1 + s2, s2, p + 1) and g(s1, s2 + s1, p + 1)
    else:
        return g(s1 + 1, s2, p + 1) or g(s1, s2 + 1, p + 1) or g(s1 + s2, s2, p + 1) or g(s1, s2 + s1, p + 1)
for x in range(1, 63):
    if g(9, x, 0):
        print(x)