def f(x, y, z):
    if x > y or (x == y and 'CAC' not in z):
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 1, y, z + 'A') + f(x * 3, y, z + 'B') + f(x + 5, y, z + 'C')
print(f(3, 69, ''))