def f(x, y, z):
    if x == y and z == 7:
        return 1
    if x != y and z == 7:
        return 0
    if z > 7:
        return 0
    if z < 7:
        return f(x - 5, y, z + 1) + f(x + 2, y, z + 1) + f(x ** 2, y, z + 1)
print(f(3, 28, 0))