def f(x, y):
    if x < y or x == 36:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 3, y) + f(x - 6, y) + f(x // 2, y)
print(f(86, 53) * f(53, 12))