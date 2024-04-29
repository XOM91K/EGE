def g(x, y):
    if x < y or x == 19:
        return 0
    if x == y:
        return 1
    if x > y:
        return g(x - 2, y) + g(x - 1, y) + g(x // 2, y)
print(g(36, 16) * g(16, 15) * g(15, 12))