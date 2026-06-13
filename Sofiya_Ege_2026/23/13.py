def f(x, y):
    if x > y: return 0
    if x == y: return 1 # 12 * 2 = 24   12 * '2' 22222222222222
    if x < y and str(x)[-1] != '1' and str(x)[-1] != '0':
        return f(x + 1, y) + f(x * int(str(x)[-1]), y)
    if x < y and (str(x)[-1] != '1' or str(x)[-1] != '0'):
        return f(x + 1, y)
print(f(24, 150))
