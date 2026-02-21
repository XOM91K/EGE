def f(x, y, s):
    if x > y or 'AB' in s:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 3, y, s + 'A') + f(x * 5, y, s + 'B') + f(x * 7, y, s + 'C')
print(f(1, 1000, ''))