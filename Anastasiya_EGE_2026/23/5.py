def f(st,fn, s):
    if st>fn or 'ab' in s:
        return 0
    elif st==fn:
        return 1
    return f(st+3, fn, s + 'a') + f(st*5, fn, s + 'b') + f(st*7, fn, s + 'c')
print(f(1,1000, ''))