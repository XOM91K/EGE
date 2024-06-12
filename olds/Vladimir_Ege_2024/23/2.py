def F(x, y):
    if x > y or x == 30:
        return 0
    elif x == y:
        return 1
    elif x < y:
        return F(x + 1, y) + F(x * 2, y)
print(F(2, 16) * F(16, 33))