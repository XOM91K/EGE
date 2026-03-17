def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        if int(str(x)[-1]) < int(str(x)[-2]):
            return f(x - 2, y) + f(int(str(x)[-1]+str(x)[-2]), y)
        else:
            return f(x - 2, y)
print(f(57, 13))