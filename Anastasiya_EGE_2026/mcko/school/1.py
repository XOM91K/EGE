def f(x, y, z):
    if x > y or x == 27 or z > 15:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 2, y, z + 1) + f(x * 3, y, z + 1) + f(x ** 3, y, z + 1)
print(f(3, 125, 0))