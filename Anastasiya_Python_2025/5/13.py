def v3(d):
    s=''
    while d>0:
        s+=str(d%3)
        d//=3
    return s[::-1]
for n in range(1, 10000):
    r=v3(n)
    if sum(map(int, r))%3==0:
        r='20'+r
    else:
        r='10'+r
    r=int(r,3)
    if r<100:
        print(n)