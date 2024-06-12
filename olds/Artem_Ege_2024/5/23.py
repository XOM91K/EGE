def tr(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
for N in range(1, 10000):
    R = tr(N)
    if N % 2 == 0:
        R = '2' + R + tr(int(R[-1]) * 2)
    else:
        R = tr(int(R[0]) * 2) + R + '2'
    R = int(R, 3)
    if R > 100:
        print(R)
