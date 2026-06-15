def is_prime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return n>1

def dels(d):
    s = []
    for x in range(2, int(d**0.5)+1):
        if d % x == 0:
            s.append(x)
            s.append(d//x)
    return sorted(set(s))
for x in range(500_001, 10**6):
    m = dels(x)
    if len(m) > 0:
        q = sum(m)
        if q ** 0.5 % 1 == 0 and is_prime(q ** 0.5):
            print(x, q)