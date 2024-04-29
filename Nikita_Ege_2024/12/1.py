def prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
for n in range(100):
    sm = 39 * 3 + n * 4
    if prime(sm):
        print(n)
        break