for n in range(0, 10000):
    s = '3' * n
    d = 0
    while '3333' in s or '222' in s:
        if '3333' in s:
            s = s.replace('3333', '2', 1)
        else:
            s = s.replace('222', '3', 1)
        d += 1
    if d == 34 and s == '22':
        print(n)