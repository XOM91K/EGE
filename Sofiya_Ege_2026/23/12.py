l = set()
def f(x, k, s):
    print(len(l))
    if k > 7: return 0
    if k == 7 and s[-1] == '2':
        l.add(x)
    return f(x + 5, k + 1, s + '1') + f(x - 3, k + 1, s + '2') + f(x + 1, k + 1, s + '3')

print(f(2, 0, ''))
