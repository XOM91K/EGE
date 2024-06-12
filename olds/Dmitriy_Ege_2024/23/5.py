def g(x, y):
    if x == y:
        return 1
    if x < y or x == 7:
        return 0
    if x > y:
        return g(x - 1, y) + g(x - 3, y) + g(x // 2, y)
print(g(19, 10) * g(10, 3))