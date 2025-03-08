def F(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        return F(x - 4, y) + F(x - 7, y) + F(int(x ** 0.5), y)
print(F(44, 22) * F(22, 3))