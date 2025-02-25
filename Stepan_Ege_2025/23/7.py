def F(x, y):
    if x < y or x == 28:
        return 0
    if x == y:
        return 1
    if x > y:
        return F(x - 3, y) + F(x // 3, y) + F(x // 2, y)
print(F(46, 20) * F(20, 3))