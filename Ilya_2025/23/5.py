def fn(x, y):
    if x < y or x == 23:
        return 0
    if x == y:
        return 1
    if x > y:
        return fn(x - 1, y) + fn(x - 5, y) + fn(x // 3, y)
print(fn(36, 21) * fn(21, 15) * fn(15, 5))