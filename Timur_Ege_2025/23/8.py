def F(x, y):
    if x < y or x == 28:
        return 0
    if x == y:
        return 1
    if x > y:
        if x % 2 == 0:
            return F(x - 2, y) + F(x // 2, y)
        else:
            return F(x - 2, y) + F(x - 3, y)
print(F(98, 1))