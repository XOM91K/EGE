def f(st, fn, s):
    if st > fn or s.count('B') > 3:
        return 0
    if st == fn:
        return 1
    if st<fn:
        return f(st + 3, fn, s + 'A') + f(st + 4, fn, s + 'B') + f(st ** 2, fn, s + 'C')
print(f(4, 61, ''))