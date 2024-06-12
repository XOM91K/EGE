for N in range(1,10000):
    s = '0'* N + '1'
    while '01' in s:
        if '1' in s:
            s = s.replace('1','10',1)
        if '01' in s:
            s = s.replace('01','1000',1)
    if 99 < s.count('0') < 1000:
        print(N, s)
        break