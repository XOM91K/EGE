for n in range(1,10000):
    r=bin(n)[2:]
    if '0' in r:
        ind = r.rindex('0')
        r = r[:ind] + r[:2] + r[ind + 1:]
        r = r[::-1]
        r=int(r,2)
        if r==123:
            print(n)