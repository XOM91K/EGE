def isPrime(x):
    for d in range(2,int(x**0.5)+1):
        if x%d==0:
            return False
    return x>1
def dels(x):
    k = []
    for d in range(1,int(x**0.5)+1):
        if x%d==0:
            k.append(d)
            k.append(x//d)
    return len(set(k)) if isPrime(len(set(k))) else 0
c = []
for x in range(int(10_000_000**0.5),int(60_000_000**0.5) + 1):
    x = x ** 2
    k = dels(x)
    if k != 0:
        c.append([x,k])
for x in sorted(c, key=lambda d: -d[1]):
    print(*x)