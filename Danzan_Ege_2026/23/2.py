def f(x, y):
    if x > y or x == 14:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 1, y) + f(x * 2, y) + f(x ** 2, y)
print(f(3, 25))