def is_prime(d):
    for x in range(2, int(d**0.5)+1):
        if d%x==0:
            return False
    return d>1
def dels(d):
    l=[]
    for x in range(1, int(d**0.5)+1):
        if d%x==0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
primes=[x for x in range(1,1000) if is_prime(x)]
d=[]
for x in range(3163, 7746):
    x = x ** 2
    l=dels(x)
    if is_prime(len(l)):
        d.append([len(l), x])
#d = sorted(d)[::-1][:7]
d = sorted(d, key=lambda d: -d[0])[:7]

for x in d:
    print(x[1], x[0])