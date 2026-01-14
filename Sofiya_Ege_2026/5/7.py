def f4(n):
    s=''
    while n>0:
        s=str(n%4)+s
        n//=4
    if s == '':
        s = '0'
    return s
d=[]
for n in range(0, 10000):
    r=f4(n)
    if n%2==0:
        r='12'+r+f4((int(r[-1]))*3)
    else:
        r='13'+r+'21'
    r=int(r, 4)
    if r>50:
        d.append(r)
print(min(d))