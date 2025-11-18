def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
k=0
for x in range(2422000, 2422080):

    if is_prime(x):
        k += 1
        print(k, x)