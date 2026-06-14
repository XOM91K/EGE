def dels(x):
    k = []

    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            k.append(d)
            k.append(x // d)
    return sum(set(k))
def isPrime(x):
    if x % 1 != 0:
        return False
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return x > 1

c = 0
for x in range(500_001,10**7):
    m = dels(x)
    if isPrime(m**0.5):
        print(x, m)
        c += 1
    if c == 5:
        break
