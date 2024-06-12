for n in range(6, 1000):
    s = '1' + '3' * n
    while '12' in s or '233' in s or '3333' in s:
        if '12' in s:
            s = s.replace('12', '332', 1)
        if '233' in s:
            s = s.replace('233', '23', 1)
        if '3333' in s:
            s = s.replace('3333', '32', 1)
    if (s.count('1') + s.count('2') * 2 + s.count('3') * 3) % 6 == 0:
        print(n)