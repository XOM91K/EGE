def f(x, y):
    if x > y or '5' in str(x):
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 1, y) + f(x * 2, y)
print(f(1, 4) * f(4, 8))