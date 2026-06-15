def f(x, y, z):
    if x > y or x == 15 or 'AA' in z:
        return 0
    if x == y:
        return 1
    return f(x - 1, y, z+'A') + f(x + 2, y, z + 'B') + f(x*2, y, z+'C')
print(f(8, 21, ''))