def F(x, y):
    if x == y:
        return 1
    if x > y or x == 25:
        return 0
    if x < y:
        return F(x + 3, y) + F(x * 2, y) + F(x * 5, y)
print(F(5, 115))
