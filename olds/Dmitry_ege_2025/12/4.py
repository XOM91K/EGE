for n in range(4, 100):
    s = '4' + '1' * n
    while '411' in s or '1111' in s:
        if '411' in s:
            s = s.replace('411', '14', 1)
        if '1111' in s:
            s = s.replace('1111', '1', 1)
    if sum(map(int, s)) > 7:
        print(n, sum(map(int, s)))