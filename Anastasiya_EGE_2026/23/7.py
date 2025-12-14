def f(st, fn):
    if st < fn or st == 8:
        return 0
    if st == fn:
        return 1
    return f(st - 1, fn) + f(st - 4, fn) + f(st // 3, fn)
print(f(19, 14) * f(14, 2))