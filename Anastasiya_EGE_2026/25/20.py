def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    l=[]
    for x in range(2, int(d**0.5)+1):
        if d%x==0:
            if is_prime(x):
                l.append(x)
            if is_prime(d // x):
                l.append(d//x)
    return sorted(set(l))

for x in range(1200001, 10**10):
    M=dels(x)
    if len(M)>1:
        M=M[0]+M[-1]
        if str(M)[-1]=='8' and M>2000:
            print(x, M)