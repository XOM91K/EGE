def g(x, y, z):
    if x > y or '11' in z or x % 10 == 0:
        return 0
    elif x == y:
        return 1
    elif x < y:
        return g(x - 1, y, z + '1') + g(x * 2, y, z + '2') + g(x * 3, y, z + '3')


print(g(5, 32, '') * g(32, 62, ''))
