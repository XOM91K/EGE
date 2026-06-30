def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y and str(x).count('1') > 0:
        return f(x + 1, y) + f(int(str(x).replace('1', '2')), y)
    else:
        return f(x + 1, y)
print(f(11, 92))