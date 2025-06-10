def div(n):
    r = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            r.add(i)
            r.add(n//i)
    return r
def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return n > 1

for x in range(1000001, 1200000):
    d=div(x)
    q = sum(d)
    if prime(q):
        print(x , q)