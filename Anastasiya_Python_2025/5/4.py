d = []
for n in range(2,1000):
    r=bin(n)[3:]
    if r.count('1')%2==0:
        r='10'+r
    else:
        r='1'+r+'0'
    r=int(r,2)
    if r<450:
        d.append(r)
print(max(d))