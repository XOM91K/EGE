def f(x, y, s):
    if x > y or 'aa' in s:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x - 1, y, s + 'a') + f(x * 2, y, s + 'b') + f(x * 3, y, s + 'c')
print(f(3, 15, ''))