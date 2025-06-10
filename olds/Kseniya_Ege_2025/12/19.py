for n in range(3, 10000):
    s ='2'+ n * '5'
    while '222' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '2', 1)
        else:
            s = s.replace('222', '5', 1)
    if sum(map(int, s)) > 23:
        print(sum(map(int, s)))