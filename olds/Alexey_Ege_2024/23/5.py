def f(x, y):
    if x < y or x == 20:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 6, y) + f(x - 1, y) + f(x // 4, y)
print(f(42, 12) * f(12, 10) * f(10, 6))