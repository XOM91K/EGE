def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
primes = []
for x in range(2, 900):
    if is_prime(x):
        primes.append(x)
for x in range(700_001, 10 ** 7):
    for y in primes:
        for z in range(2, 20):
            if y ** z == x:
                print(x, y)
                break