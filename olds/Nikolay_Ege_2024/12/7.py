for n in range(1, 1000):
    s = '1' + '2' * n + '3' * 2 * n + '1'
    while '11' in s or '22' in s or '33' in s:
        if '11' in s:
            s = s.replace('11', '23', 1)
        if '22' in s:
            s = s.replace('22', '13', 1)
        if '33' in s:
            s = s.replace('33', '12', 1)
    if sum(map(int, s)) == 502:
        print(n)
        break
