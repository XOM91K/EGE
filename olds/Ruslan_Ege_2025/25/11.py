def is_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return n > 1
def div(n):
    r = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            if is_prime(i):
                r.add(i)
            if is_prime(n // i):
                r.add(n//i)
    return sorted(r)
for x in range(1200000, 1500000):
    d = div(x)
    m = 0
    if len(d) > 0:
        m = d[0]+d[-1]
    if m > 2000 and str(m)[-1] == '8':
        print(x, m)