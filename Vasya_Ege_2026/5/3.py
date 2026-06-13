for n in range(11,100000):
    r = bin(n)[2:]
    if r.count('11') == 1:
        r = '10' + r[2:] + '0'
    else:
        r = '11' + r[2:] + '1'
    r = int(r,2)
    if r <= 1500 and r > 1490:
        print(n, r)