def f(x, y, s):
    if x > y or 'ca' in s:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 2, y, s + 'a') + f(x + 3, y, s + 'b') + f(x * 4, y, s + 'c')
print(f(1, 50, ''))