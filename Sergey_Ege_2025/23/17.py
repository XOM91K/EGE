def f(x, y, s):
    if x < y or 'AAA' in s or 'BBB' in s:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 2, y, s + 'A') + f(x // 2 if x % 2 == 0 else x - 7, y, s + 'B')
print(f(40, 1, ''))