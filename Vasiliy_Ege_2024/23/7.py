def g(x, y):
    if x == y:
        return 1
    if x > y or x == 21:
        return 0
    if x < y:
        return g(x + 1, y) + g(x * 2, y) + g(x * 3, y)


print(g(2, 9) * g(9, 37))