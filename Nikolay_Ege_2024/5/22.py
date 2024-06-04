def v7(n):
    s = ''
    while n > 0:
        s += str(n % 7)
        n //= 7
    return s[::-1]
for N in range(1, 10000):
    R = v7(N)
    if N % 7 == 0:
        R += R[-2:]
    else:
        R += v7(N % 7 * 2)
    R = int(R, 7)
    if R < 220:
        print(N)