def g(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    elif x < y:
        return g(x + 1, y) + g(x * 2, y)
print(g(1, 12) * g(12, 25) * g(25, 40))