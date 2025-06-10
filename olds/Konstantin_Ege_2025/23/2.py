def g(x, y):
    if x == y:
        return 1
    if x > y or x == 20:
        return 0
    if x < y:
        return g(x + 1, y) + g(x + 3, y) + g(x ** 2, y)
print(g(2, 15) * g(15, 35))