A=[]
for n in range(0,1000):
    r=bin(n)[2:]
    if n%3==0:
        r=r.replace('0','11')
    else:
        r=r.replace('1','10')
    if int(r,2)<=161:
        A.append(int(r,2))
print(max(A))