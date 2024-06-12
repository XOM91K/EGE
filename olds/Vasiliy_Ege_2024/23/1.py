def g(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    if x < y:
        return g(x + 1, y) + g(x + 2, y)
print(g(1, 4))