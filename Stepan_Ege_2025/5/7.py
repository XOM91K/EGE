def v3(d):
    R = ''
    while d > 0:
        R += str(d % 3)
        d //= 3
    return R[::-1]

for N in range(1, 10000):
    R = v3(N)
    if N % 3 == 0:
        R = '1' + R + '02'
    else:
        R += v3(N % 3 * 4)
    R = int(R, 3)
    if R < 199:
        print(N)