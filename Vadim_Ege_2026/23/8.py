l = []
def f(x, s):
    if len(s) > 7:
        return 0
    elif len(s) == 7 and s[-1] == 'B':
        l.append(x)
        return 1
    else:
        return f(x + 5, s + 'A') + f(x - 3, s + 'B') + f(x + 1, s + 'C')
print(f(2, ''))
print(len(set(l)))