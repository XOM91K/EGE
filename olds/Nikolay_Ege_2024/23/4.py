def f(x, y):
    if x == y:
        return 1
    if x < y or x == 27:
        return 0
    if x > y:
        return f(x - 1, y) + f(x - 5, y)
print(f(32, 26) * f(26, 24) * f(24, 17))