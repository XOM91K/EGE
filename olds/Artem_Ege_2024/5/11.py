def tr(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
for N in range(1, 10000):
    R = tr(N)
    if N % 3 == 0:
        R = '1' + R + '02'
    else:
        R += tr(N % 3 * 4)
    if int(R, 3) < 199:
        print(N)