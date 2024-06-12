def f(x, y, z):
    if x == y and z < 4:
        return 1
    if x > y or x == 10 or x == 38 or z > 3:
        return 0
    if x < y:
        return f(x + 1, y, z + 1) + f(x + 2, y, z) + f(x * 3, y, z)
print(f(1, 25, 0) * f(25, 43, 0))