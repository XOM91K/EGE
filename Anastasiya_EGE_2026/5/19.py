def v4(d):
    s=''
    while d>0:
        s+=str(d%4)
        d//=4
    return s[::-1]

for n in range(1, 10000):
    r=v4(n)
    if len(r)%2==0: # 6  0 1 2    0   3 4 5
        r=r[:len(r) // 2] + '0' + r[len(r) // 2:]
    else:
        r=r
    if int(r)<=180:
        print(r,n)