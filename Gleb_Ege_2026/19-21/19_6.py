def g(s, p):
    if p == 2 and s <= 19:
        return 1
    if p == 2 and s > 19:
        return 0
    if p < 2 and s <= 19:
        return 0

    if p % 2 == 0:
        return g(s - 1, p + 1) and g(s // 3 if s % 3 == 0 else s - 2, p + 1) and g(s // 5 if s % 5 == 0 else s - 3, p + 1)
    else:
        return g(s - 1, p + 1) or g(s // 3 if s % 3 == 0 else s - 2, p + 1) or g(s // 5 if s % 5 == 0 else s - 3, p + 1)
for s in range(20, 200):
    if g(s, 0):
        print(s)