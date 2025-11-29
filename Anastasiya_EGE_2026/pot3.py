def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
pr = 1
for x in range(2, 20):
    if is_prime(x):
        pr *= x
print(pr)