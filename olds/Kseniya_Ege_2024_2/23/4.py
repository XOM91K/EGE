def g(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    if x < y:
        return g(x + 1, y) + g(x + 3, y) + g(x * 3, y)
print(g(3, 9) * g(9, 27) * g(27, 31))