for n in range(4, 1000):
    s = '5' + '2' * n
    while '52' in s or '222' in s or '122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '222' in s:
            s = s.replace('222', '15', 1)
        if '122' in s:
            s = s.replace('122', '21', 1)
    if int(sum(map(int, s)) ** 0.5) ** 2 == sum(map(int, s)):
        print(sum(map(int, s)), n)
