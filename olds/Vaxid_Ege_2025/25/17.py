def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
ct = 0
for x in range(2422000, 2422081):
    if is_prime(x):
        ct += 1
        print(ct, x)
