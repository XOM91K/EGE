def is_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return n > 1
d = []
for c1 in range(0, 300):
    for c2 in range(0, 300):
        sm = c2 * 3 + c1 * 4
        sm_do = c1 + c2 * 2
        if c1 + c2 > 39:
            if is_prime(sm):
                d.append(sm_do)
print(min(d))
