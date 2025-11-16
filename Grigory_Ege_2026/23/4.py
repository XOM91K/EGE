def f(x, y):
    if x < y or x == 23:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 1, y) + f(x - 5, y) + f(x // 3, y)
print(f(36, 21) * f(21, 15) * f(15, 5))