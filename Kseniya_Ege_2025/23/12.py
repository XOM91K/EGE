def f(x, y):
    if x < y or x == 15:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 2, y) + f(x - 3, y) + f(x // 3, y)
print(f(48, 25) * f(25, 17) * f(17, 4))