for n in range(1,1000):
    r = bin(n)[2:]
    if n % 2 == 0 :
        r = r + '0'
    else:
        r = r + '1'
    if r.count('1') % 2 ==0 :
        r = r +'0'
    else:
        r = r+'1'
    r = int(r, 2)
    if r>2023:
        print(r)