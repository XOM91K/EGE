for n in range(101, 200):
    s = '3' * n
    while '111' in s or '333' in s:
        if '111' in s:
            s = s.replace('111', '3', 1)
        else:
            s = s.replace('333', '1', 1)
    print(s, n)