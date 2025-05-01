def F(x, y):
    if x > y or x == 56:
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x + 3, y) + F(x + 7, y) + F(x * 3, y)
print(F(12, 40) * F(40, 72) * F(72, 89))