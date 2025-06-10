def f(x, y):
    if x > y or x == 59:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 1, y) + f(x * 2, y)
print(f(3, 14) * f(14, 62))