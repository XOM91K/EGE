def v3(n):
    ost = ''
    while n > 0:
        ost += str(n % 3)
        n = n // 3
    return ost[::-1]

for N in range(1, 1000):
    R = v3(N)
    if sum([int(d) for d in R]) % 2 == 0:
        R = R + '0'
        R = '2' + R[2:]
    else:
        R = R + '1'
        R = '20' + R[2:]
    if int(R, 3) > 75:
        print(N, int(R, 3))