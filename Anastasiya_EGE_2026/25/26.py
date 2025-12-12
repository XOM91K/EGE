def dels(d):
    l=[]
    for x in range(2, int(d**0.5)+1):
        if d%x==0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))

def is_prime(d):
    for x in range(2, int(d**0.5)+1):
        if d%x==0:
            return False
    return d>1

for x in range(1000001, 10**10):
    Q = dels(x)
    if len(Q) > 1:
        Q = sum(Q)
        if is_prime(Q):
            print(x, Q)
