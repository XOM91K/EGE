def g(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        return g(x - 2, y) + g(x // 2, y)


print(g(38, 10) * g(10, 2))
