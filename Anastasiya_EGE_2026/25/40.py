def is_prime(d):
    for x in range(2,int(d**0.5)+1):
        if d%x==0:
            return False
    return d>1
def dels(d):
    s=[]
    for x in range(1,int(d**0.5)+1):
        if d%x==0 and is_prime(x) and ('3' in str(x) and '5' in str(x)):
            s.append(x)
        if d % x == 0 and is_prime(d//x) and ('3' in str(d//x) and '5' in str(d//x)):
            s.append(d//x)
    return sorted(set(s))
for x in range(4_000_001,10**8):
    d=dels(x)
    if len(d)==2 and (d[0]*d[1]*d[1]==x or d[0] * d[0] * d[1] == x):
        print(x,max(d))