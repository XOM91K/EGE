def v6(n):
    s = ''
    while n > 0:
        s += str(n % 6)
        n //= 6
    return s[::-1]
for N in range(1, 10000):
    R = v6(N)
    if N % 3 == 0:
        R += R[:2]
    else:
        R += v6(N % 3 * 10)
    if int(R, 6) > 680:
        print(int(R, 6))