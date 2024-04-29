for n in range(0, 1000):
    s = '7' + (n + 1) * '1' + (n + 2) * '2' + (n + 3) * '3'
    while '71' in s or '72' in s or '73' in s:
        if '71' in s:
            s = s.replace('71', '227', 1)
        if '72' in s:
            s = s.replace('72', '37', 1)
        if '73' in s:
            s = s.replace('73', '17', 1)
    if sum(map(int, s)) == 9 * n:
        print(n)