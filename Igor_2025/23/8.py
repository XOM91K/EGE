def f(x, y):
    if x < y or x == 16:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 2, y) + f(x // 3 if x % 3 == 0 else x - 4, y)
print(f(36, 4))