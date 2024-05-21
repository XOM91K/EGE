
#CAC
def f(x, y, z):
    fl = 0
    if x == y:
        for i in range(len(z) - 3):
            if z[i + 3] - z[i] == 11:
                fl = 1
                break
    if x > y or (x == y and fl == 0):
        return 0
    if x == y:
        return 1
    return f(x + 1, y, z + [x + 1]) + f(x * 3, y, z + [x * 3]) + f(x + 5, y, z + [x + 5])
print(f(3, 69, []))