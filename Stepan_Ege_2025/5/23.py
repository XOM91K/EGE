def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
for N in range(1, 10000):
    R = v3(N)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        R = R + v3(sum(map(int, R)))
    R = int(R, 3)
    if R > 278 and R % 2 != 0:
        print(R)