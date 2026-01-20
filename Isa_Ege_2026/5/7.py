for n in range(1, 10000):
    r=bin(n)[2:]
    if n%3 != 0:
        r = '10' + r + '0'
    else:
        r = '1' + r[:-2] + '11'
    r=int(r,2)
    if r > 999 and n % 2 == 0:
        print(r)