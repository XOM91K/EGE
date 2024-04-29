def F(x, y):
    #x = 1     y = 21
    if x > y or x == 10:
        return 0
    elif x == y:
        return 1
    elif x < y:
        return F(x + 1, y) + F(x * 2, y)
print(F(1, 21))