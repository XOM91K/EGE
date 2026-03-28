def g(s, p):
    if s <= 505 and  (p==4 or p == 2):
        return 1
    if s > 505 and p == 4:
        return 0
    if s <= 505 and p != 4:
        return 0

    if p % 2 != 0:
        return g(s - 3, p + 1) or g(s // 5, p + 1)
    else:
        return g(s - 3, p + 1) and g(s // 5, p + 1)


for S in range(500, 100000):
    if g(S, 0):
        print(S)