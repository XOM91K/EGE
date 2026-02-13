def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 2, y) + f(x * 4, y)
print(f(3, 200) * f(200, 510))