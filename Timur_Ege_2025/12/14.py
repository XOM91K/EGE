for n in range(4, 1000):
    s = '3' + '5' * n
    while '333' in s or '555' in s:
        if '555' in s:
             s = s.replace('555', '35', 1)
        else:
             s = s.replace('333', '53', 1)
    if len(s) > 17:
        print(len(s))