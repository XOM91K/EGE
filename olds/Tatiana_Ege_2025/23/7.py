def f(x, y, d):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        if d != 1:
            return f(x + 3, y, 1) + f(x * 5, y, 2) + f(x * 7, y, 3)
        else:
            return f(x + 3, y, 1) + f(x * 7, y, 3)
print(f(1, 1000, 0))