def F(x, y, z):
    if x > y or 'CA' in z:
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x + 2, y, z + 'A') + F(x + 3, y, z + 'B') + F(x * 4, y, z + 'C')
print(F(1, 50, ''))