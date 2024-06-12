for n in range(20, 21):
    s = '1' * 40 + '2' * 40 + '3' * n
    while '23' in s or '12' in s or '32' in s:
        if '12' in s:
            s = s.replace('12', '21', 1)
        if '32' in s:
            s = s.replace('32', '1', 1)
        if '23' in s:
            s = s.replace('23', '2', 1)
    #if s.count('1') + s.count('2') * 2 + s.count('3') * 3 == 100:
    print(n, s, s.count('1') + s.count('2') * 2 + s.count('3') * 3)

