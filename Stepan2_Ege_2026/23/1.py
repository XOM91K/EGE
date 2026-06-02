def f(x, y):
    if x < y or x == 73:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 3, y) + f(x - 8, y) + f(x // 2, y)
print(f(76, 41) * f(41, 12))