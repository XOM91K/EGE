def g(x, y, s):
    if x > y or x == 15 or 'AA' in s:
        return 0
    if x == y:
        return 1
    else:
        return g(x - 1, y, s + 'A') + g(x + 2, y, s + 'B') + g(x * 2, y, s + 'C')
print(g(8, 21, ''))