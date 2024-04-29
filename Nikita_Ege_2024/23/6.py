def F(x, y):
    if x > y or x == 15:
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x + 1, y) + F(x + 3, y) + F(x * 2, y)
print(F(1, 9) * F(9, 27))