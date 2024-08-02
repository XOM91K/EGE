def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 1, y) + f(x - 2, y) + f(x // 3, y)
print(f(16, 11) * f(11, 6))