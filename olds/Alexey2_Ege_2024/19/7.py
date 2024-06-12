def g(s, p):
    if s == 42 and p == 3:
        return 1
    elif s != 42 and p == 3:
        return 0
    elif s == 42 and p < 3:
        return 0
    if p % 2 == 0:
        if s + 7 <= 42:
            return g(s + 1, p + 1) or g(s + 3, p + 1) or g(s + 7, p + 1)
        elif s + 3 <= 42:
            return g(s + 1, p + 1) or g(s + 3, p + 1) or g(s - 7, p + 1)
        elif s + 1 <= 42:
            return g(s + 1, p + 1) or g(s - 3, p + 1) or g(s - 7, p + 1)
        elif s - 7 >= 42:
            return g(s - 1, p + 1) or g(s - 3, p + 1) or g(s - 7, p + 1)
        elif s - 3 >=42:
            return g(s - 1, p + 1) or g(s - 3, p + 1)
        elif s - 1 >= 42:
            return g(s - 1, p + 1)
    else:
        if s + 7 <= 42:
            return g(s + 1, p + 1) and g(s + 3, p + 1) and g(s + 7, p + 1)
        elif s + 3 <= 42:
            return g(s + 1, p + 1) and g(s + 3, p + 1) and g(s - 7, p + 1)
        elif s + 1 <= 42:
            return g(s + 1, p + 1) and g(s - 3, p + 1) and g(s - 7, p + 1)
        elif s - 7 >= 42:
            return g(s - 1, p + 1) and g(s - 3, p + 1) and g(s - 7, p + 1)
        elif s - 3 >= 42:
            return g(s - 1, p + 1) and g(s - 3, p + 1)
        elif s - 1 >= 42:
            return g(s - 1, p + 1)
for S in range(1, 100):
    if g(S, 0):
        print(S)