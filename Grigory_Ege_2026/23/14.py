def F(x, y, s):
    if 'AA' in s or x == 15:
        return 0
    if x > y and 'AA' not in s:
        return F(x - 1, y, s + 'A')
    if x == y:
        return 1
    if x < y:
        return F(x - 1, y, s + 'A') + F(x + 2, y, s + 'B') + F(x * 2, y, s + 'C')
print(F(8, 20, ''))