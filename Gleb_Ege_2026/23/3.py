def F(x, y):
    if x < y or x == 24:
        return 0
    if x == y:
        return 1
    if x > y:
        return F(x - 2, y) + F(x - 3, y) + F(x // 4, y)
print(F(36, 13))