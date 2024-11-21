def f(x, y): # x - начальное число y - конечное число
    if x < y or x == 24:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 2, y) + f(x - 3, y) + f(x // 4, y)
print(f(36, 13))


