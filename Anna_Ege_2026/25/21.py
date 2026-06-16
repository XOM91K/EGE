import math, itertools
def is_prime(n):
    for x in range(2, int(n ** 0.5)+1):
        if n % x == 0:
            return False
    return n > 1

def dels(d):
    s = []
    for x in range(1, int(d ** 0.5)+1):
        if d % x == 0:
            if is_prime(x) and str(x).count('2') == 1:
                s.append(x)
            if is_prime(d//x) and str(d//x).count('2') == 1:
                s.append(d//x)
    return s[::-1]
for x in range(220262027, 225000000):
    m = dels(x)
    if len(m)>3:
        if x == math.prod(m):
            print(x, max(m))
