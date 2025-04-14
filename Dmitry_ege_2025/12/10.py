for n in range(3, 1000):
    s = '3' + '1' * n
    while '31' in s or '211' in s or '1111' in s:
        if '31' in s:
            s = s.replace('31', '1', 1)
        if '211' in s:
            s = s.replace('211', '13', 1)
        if '1111' in s:
            s = s.replace('1111', '2', 1)
    if sum(map(int,s)) == 15:
        print(n)