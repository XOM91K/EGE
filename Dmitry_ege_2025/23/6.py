def F(x, y):
    if x > y or x == 24:
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x + 3, y) + F(x + 8, y) + F(x * 3, y)
print(F(13, 22) * F(22, 33) * F(33, 81))