def v3(n):
    s=''
    while n>0:
        s+=str(n%3)
        n//=3
    return s[::-1]
for n in range(1,10000):
    r=v3(n)
    if n%7==0:
        r+=r[-2:]
    else:
        r+= v3(3*(n%3))
    r=int(r,3)
    if r>369:
        print(r)