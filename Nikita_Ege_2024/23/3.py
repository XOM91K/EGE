def F(x, y, s):
    if x > y or ('11' in s or '22' in s):
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x + 1, y, s + '1') + F(x + 3, y, s + '1') + F(x * 2, y, s + '2') + F(x * 3, y, s + '2')
print( F(1, 9999, ''))