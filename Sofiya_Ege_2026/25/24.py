def q(d):
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
for x in range(10**6, 10**10):
    if is_prime(sum(q(x))):
        print(x, sum(q(x)))