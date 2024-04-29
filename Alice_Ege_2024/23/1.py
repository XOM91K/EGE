def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    if x < y:
        return f(x + 3, y) + f(x * 4, y) + f(x + 4, y)
print(f(11, 20) * f(20, 55))