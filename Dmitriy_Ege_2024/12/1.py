for x in range(101, 500):
    s = '3' * x
    while '111' in s or '333' in s:
        if '111' in s:
            s = s.replace('111', '3', 1)
        else:
            s = s.replace('333', '1', 1)
    print(x, s)
