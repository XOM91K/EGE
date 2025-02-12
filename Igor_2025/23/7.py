def f(x, y):
    if x < y or x == 12:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 3, y) + f(x // 2 if x % 2 == 0 else x - 5, y)
print(f(36, 3))