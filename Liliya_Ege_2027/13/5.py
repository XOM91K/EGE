def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 3, y) + f(x + int(sorted(str(x))[-1]), y)
print(f(10, 24) * f(24, 41))