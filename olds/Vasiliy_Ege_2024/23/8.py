def g(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    if x < y:
        return g(x * 2, y) + g(x * 3, y)
print(g(8, 96) * g(96, 3456))