def isPrime(x):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return x > 1


def dels(x):
    k = []
    for d in range(1, int(x ** 0.5) + 1):
        if x % d == 0:
            if isPrime(d) and ('4' in str(d) or '7' in str(d)):
                k.append(d)
            if isPrime(x // d) and ('4' in str(x // d) or '7' in str(x // d)):
                k.append(x // d)
    return sorted(set(k))


c = 0
for x in range(2_400_001, 10 ** 7):
    m = dels(x)
    if len(m) == 3 and (m[0] * m[1] * m[2] == x):
        print(x, max(m))
        c += 1
    if c == 5:
        break
