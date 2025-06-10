def f(x, y):
    if x < y or x == 28:
        return 0
    if x == y:
        return 1
    if x > y and x % 2 == 0:
        return f(x - 2, y) + f(x // 2, y)
    else:
        return f(x - 2, y) + f(x - 3, y)
print(f(98, 1))