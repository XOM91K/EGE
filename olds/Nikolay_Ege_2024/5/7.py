def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
for N in range(10, 10000):
    R = v3(N)
    if N % 2 == 0:
        R += R[-2:]
    else:
        R += v3(sum(map(int, R)))
    print(int(R, 3), N)