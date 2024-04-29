for n in range(4,1000):
    s = '5' + '2' * n
    while '52' in s or '222' in s or '122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '222' in s:
            s = s.replace('222', '15', 1)
        if '122' in s:
            s = s.replace('122', '21', 1)
    s = s.replace('>', '1', 1)
    sum1 = s.count('1') + s.count('2') * 2 + s.count('5') * 5
    if sum1 ** 0.5 % 1 == 0:
        print(n, sum1 ** 0.5)