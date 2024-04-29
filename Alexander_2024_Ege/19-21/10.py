def g(s, p):
    if s <= 0 and (p == 4 or p == 2):
        return 1
    elif s > 0 and p == 4:
        return 0
    elif s <= 0:
        return 0
    if p % 2 == 0:
        if s - 5 >= 0:
            return g(s - 5, p + 1) and g(s // 3, p + 1)
        else:
            return g(s // 3, p + 1)
    else:
        if s - 5 >= 0:
            return g(s - 5, p + 1) or g(s // 3, p + 1)
        else:
            return g(s // 3, p + 1)
for S in range(1, 1000):
    if g(S, 0):
        print(S)
#7
#11 23