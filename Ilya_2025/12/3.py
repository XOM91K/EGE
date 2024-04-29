def prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True
for n in range(1, 100):
    s = 39 + 78 + n * 4
    if prime(s):
        print(n, s, prime(s))

