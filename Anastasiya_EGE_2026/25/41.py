def is_prime(d):
    for x in range(2, int(d**0.5)+1):
        if d % x == 0:
            return False
    return d>1

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
            print(x,q)