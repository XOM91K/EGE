def g(x, y):
    if x > y or x == 17:
        return 0
    elif x == y:
        return 1
    return g(x + 1, y) + g(x * 2, y)
print(g(1, 10) * g(10, 35))

