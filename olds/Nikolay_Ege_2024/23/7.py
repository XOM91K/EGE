def f(x, y, z):
    if x > y or 'AB' in z:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 3, y, z + 'A') + f(x * 5, y, z + 'B') + f(x * 7, y, z + 'C')


print(f(1, 1000, ''))
