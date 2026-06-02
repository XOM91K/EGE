l = []
def f(x, ct, s):
    global l
    if ct == 8:
        return 0
    if ct == 7 and s[-1] == 'B':
        l.append(x)
        l = sorted(set(l))
        print(len(l), l)
        return 1
    return f(x + 5, ct + 1, s + 'A') + f(x - 3, ct + 1, s + 'B') + f(x + 1, ct + 1, s + 'C')
print(f(2, 0, ''))