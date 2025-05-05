def F(x, y, z):
    if x > y or str(x)[-1] == '3' or 'AA' in z:
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x - 1, y, z + 'A') + F(x - 5, y, z + 'A') + F(x + 7, y, z + 'B') + F(x * 2, y, z + 'B')
print(F(9, 60, '') * F(60, 84, ''))