for n in range(1, 10000):
    s = '1' + '0' * n
    while '10' in s or '1' in s:
        if '10' in s:
            s = s.replace('10', '001', 1)
        elif '1' in s:
            s = s.replace('1', '0')
    if 100 <= len(s) <= 999:
        print(n)
        break

