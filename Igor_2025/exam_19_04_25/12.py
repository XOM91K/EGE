


for n in range(3, 10_000+1):
    s = '4' + '2'*n
    while '42' in s or '8222' in s or '2222' in s:
        if '42' in s:
            s = s.replace('42', '2', 1)
        if '8222' in s:
            s = s.replace('8222', '24', 1)
        if '2222' in s:
            s = s.replace('2222', '8', 1)
    if sum([int(i) for i in s]) == 110:
        print(n)
        exit()
