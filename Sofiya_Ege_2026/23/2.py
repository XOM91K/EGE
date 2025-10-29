def f(x, y, s):
    if x > y or '31' in s:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 2, y, s + '1') + f(x + 3, y, s + '2') + f(x * 4, y, s + '3')
print(f(1, 50, ''))