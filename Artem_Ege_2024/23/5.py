def F(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return F(x + 1, y) + F(x + 2, y) + F(x * 2, y)
print(F(4, 11) * F(11, 13) * F(13, 15))