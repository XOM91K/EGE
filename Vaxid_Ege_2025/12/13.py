for n in range(4, 10000):
    s = '4' * 10 + '7' * n
    while '47' in s or '4747' in s or '774' in s:
        if '47' in s:
            s = s.replace('47', '777', 1)
        if '4747' in s:
            s = s.replace('4747', '444', 1)
        if '774' in s:
            s = s.replace('774', '477', 1)
    if sum(map(int, s)) % n == 0:
        print(n)