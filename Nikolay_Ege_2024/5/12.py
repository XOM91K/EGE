for n in range(1, 10000):
    r = bin(n)[2:]
    if r[0] != '0':
        r2 = r
        if r2.count('1') > r2.count('0'):
            r2 += '0'
        else:
            r2 += '11'
        if int(r2, 2) > 2019:
            print(n)