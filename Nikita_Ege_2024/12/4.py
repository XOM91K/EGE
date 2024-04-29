mx = 0
for n in range(1000, 3, -1):
    s = '5' + '2' * n
    while '52' in s or '222' in s or '122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '222' in s:
            s = s.replace('222', '15', 1)
        if '122' in s:
            s = s.replace('122', '21', 1)
    sm = sum(map(int, s))
    if int((sm ** 0.5)) ** 2 == sm:
        print(n)