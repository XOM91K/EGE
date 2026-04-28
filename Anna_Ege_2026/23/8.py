def f(x, y, s):
    if ('11' in s or str(x)[-1] == '3') or x > y:
        return 0
    elif x == y:
        return 1
    if x < y:
        return f(x - 1, y, s + '1') + f(x - 5, y, s + '1') + f(x + 7, y, s + '2') + f(x * 2, y, s + '2')
print(f(9, 60, '') * f(60, 84, ''))