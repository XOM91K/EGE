def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
n = 5700000
for x in range(2, n + 1):
    if is_prime(x) and is_prime(n - x):
        print(x, n - x)
        break
