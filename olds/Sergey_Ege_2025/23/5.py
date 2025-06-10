def f(x, y):
    if x > y or x == 70:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x * 3, y) + f(x + 5, y) + f(x * 4, y)
print(f(6, 79))