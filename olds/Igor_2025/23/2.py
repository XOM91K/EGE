def f(x, y):
    # x: начальное число
    # y: конечное число
    if x > y or x == 20:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 3, y) + f(x ** 2, y)
print(f(3, 23) * f(23, 25))