for n in range(1, 100):
    s = '7' + '1' * (n + 1) + '2' * (n + 2) + '3' * (n + 3)
    while '71' in s or '72' in s or '73' in s:
        if '71' in s:
            s = s.replace('71', '227', 1)
        if '72' in s:
            s = s.replace('72', '37', 1)
        if '73' in s:
            s = s.replace('73', '17', 1)
    if (s.count('1') + s.count('2') * 2 + s.count('3') * 3 + s.count('7') * 7) == n * 9:
        print(n, s.count('1') + s.count('2') * 2 + s.count('3') * 3 + s.count('7') * 7)