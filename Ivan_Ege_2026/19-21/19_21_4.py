import sys

sys.setrecursionlimit(9999999)


def g(s, p):
    if s <= 25 and (p == 2 or p == 4):
        return 1
    elif s > 25 and p == 4:
        return 0
    elif s <= 25 and p < 4:
        return 0
    if p % 2 == 0:
        return g(s - 4, p + 1) and g(s - 6, p + 1) and g(s // 3, p + 1)
    else:
        return g(s - 4, p + 1) or g(s - 6, p + 1) or g(s // 3, p + 1)


for s in range(27, 1000):
    if g(s, 0):
        print(s)
