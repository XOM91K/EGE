def f(x, y):
    if x > y or x == 17:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x * 4, y) + f(x + 3, y) + f(x + 2, y)
print(f(7, 38) * f(38, 40) * f(40, 56))