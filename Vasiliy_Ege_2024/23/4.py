def g(x, y):
    if x == y:
        return 1
    if x > y or x == 17 or x == 32 or x == 50:
        return 0
    if x < y:
        return g(x + 1, y) + g(x + 5, y) + g(x ** 2, y)


print(g(5, 25) * g(25, 45) * g(45, 60))