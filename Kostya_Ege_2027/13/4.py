def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        if int(str(x)[-2]) > int(str(x)[-1]):
            return f(x - 3, y) + f(int(str(x)[:-2] + str(x)[-1] + str(x)[-2]), y)
        else:
            return f(x - 3, y)
print(f(1001, 959) * f(959, 902))