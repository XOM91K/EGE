def g(x, y):
    if x > y or x == 13:
        return 0
    elif x == y:
        return 1
    elif x < y:
        return g(x + 1, y) + g(x + 5, y) + g(x * 2, y)
print(g(7, 25))