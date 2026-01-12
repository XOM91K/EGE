def is_prime(d):
    for x in range(2, int(d**0.5)+1):
        if d%x==0:
            return False
    return d>1
primes = [x for x in range(1, 1000) if is_prime(x)]
print(primes)
for x in range(700_000, 10**6):
    for y in range(2, 30):
        for z in primes:
            if x==z**y:
                print(x, z)