def f(x, y):
    if x == y:
        return 1
    if x == 28 or x < y:
        return 0
    if x > y:
        return f(x - 3, y) + f(x - 5, y) + f(x // 3, y)
print(f(41, 12))
