def v4(d):
    s=''
    while d>0:
        s+=str(d%4)
        d//=4
    return s[::-1] if s != '' else '0'
mn=[]
for n in range(0,10000):
    r=v4(n)
    if n%2==0:
        r='12'+r+v4(3*int(r[-1]))
    else:
        r='13'+r+'21'
    r=int(r,4)
    if r>50:
        mn.append(r)
print(min(mn))