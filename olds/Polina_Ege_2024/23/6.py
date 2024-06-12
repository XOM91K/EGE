def f(x, y):
    if x == y:
        return 1
    elif x < y:
        return 0
    elif x > y:
        if x ** 0.5 == int(x ** 0.5):
            return f(x - 2, y) + f(x - 3, y) + f(int(x ** 0.5), y)
        else:
            return f(x - 2, y) + f(x - 3, y)
print(f(25, 3))
