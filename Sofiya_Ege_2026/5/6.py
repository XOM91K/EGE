def f16(n):
    s=[]
    while n>0:
        s.append(n%16)
        n//=16
    return s[::-1]

for n in range(3, 10000):
    r=hex(n)[2:]
    smcif = 0
    # ff882
    for y in '0123456789abcdef':
        smcif += r.count(y) * int(y, 16)
    if smcif %2 == 0:
        r += 'f'
    else:
        r += '1'
    r=int(r, 16)
    if r<=300:
        print(n)