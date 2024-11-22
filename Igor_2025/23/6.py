def f(x, y, z):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        if z == 'C':
            return f(x + 3, y, 'B') + f(x * 4, y, 'C')
        else:
            return f(x + 2, y, 'A') + f(x + 3, y, 'B') + f(x * 4, y, 'C')
print(f(1, 50, ''))