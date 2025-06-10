def is_prime(d):
    for x in range(2, d):
        if d % x == 0:
            return False
    return d > 1
mn = 10 ** 10
for x in range(0, 100):
    for y in range(0, 100):
        if x + y > 40:
            sm1 = 3 * x + 4 * y
            sm2 = 2 * x + y
            if is_prime(sm1):
                mn = min(mn, sm2)
print(mn)