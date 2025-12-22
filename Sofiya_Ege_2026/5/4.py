for n in range(2, 10000):
    r = bin(n)[2:]
    r = r[1:]
    if r.count('1') % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '0'
    r = int(r, 2)
    if r < 450:
        print(r)