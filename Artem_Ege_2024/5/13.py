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
    R = int(R, 6)
    if R > 680:
        print(R)