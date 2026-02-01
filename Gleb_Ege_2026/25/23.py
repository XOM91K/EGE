def f(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return n > 1
primes = [x for x in range(2, 1000) if f(x)]
print(primes, len(primes))
for x in range(700001, 1000000):
    for y in primes:
        for z in range(2, 15):
            if y ** z == x:
                print(x, y)