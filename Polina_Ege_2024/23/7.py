def f(x, y, z):
    if x > y or '22' in z:
        return 0
    elif x == y:
        return 1
    elif x < y:
        return f(x + 1, y, z + '1') + f(x + 3, y, z + '2') + f(x * 2, y, z + '3')
print(f(2, 20, ''))
