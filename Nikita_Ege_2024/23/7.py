def f(x, y):
    if x == 11:
        return 0
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 1, y) + f(x + 4, y) + f(x * 3, y)
print(f(7, 27) * f(27, 42))