def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 3, y) + f(x + 4, y) + f(x ** 2, y)
print(f(4, 7) * f(7, 18) * f(18, 41))