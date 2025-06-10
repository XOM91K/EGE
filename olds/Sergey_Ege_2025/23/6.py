def f(x, y):
    if x > y or x == 23:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 2, y) + f(x * 3, y) + f(x * 5, y)
print(f(1, 13) * f(13, 75))