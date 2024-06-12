def v3(n):
    s=''
    while n>0:
        s+=str(n%3)
        n//=3
    return s[::-1]
a=[]
for n in range(1,10000):
    r=v3(n)
    if sum(map(int,r))%4==0:
        r='1'+r[:-2]
    else:
        r+=v3((sum(map(int,r))%4)*3)
    if int(r,3)>353:
        a.append(int(r,3))
print(min(a))
s='5777'
print(s[:2])