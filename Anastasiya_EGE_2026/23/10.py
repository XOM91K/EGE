def f(st, fn, s):
    if st > fn or ('AA' in s) or st==15:
        return 0
    if st == fn:
        return 1
    return f(st-1, fn, s + 'A') + f(st+2, fn, s + 'B') + f(st*2, fn, s + 'C')
print(f(8, 21, ''))