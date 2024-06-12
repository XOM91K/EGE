def tr(n):
    ost = ''
    while n > 0:
        ost += str(n % 3)
        n //= 3
    return ost[::-1]
for N in range(1, 1000):
    trc = tr(N)
    if N % 4 == 0:
        trc += trc[-3:]
    else:
        trc += tr((N % 4) * 4)
    if int(trc, 3) < 127:
        print(int(trc, 3))