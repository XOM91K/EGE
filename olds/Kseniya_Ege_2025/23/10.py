def f(x, y):
    if x < y or x == 15:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 2, y) + f(x - 5, y) + f(x // 3, y)
print(f(50, 35) * f(35, 20) * f(20, 8))