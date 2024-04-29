def vtr(d):
    s = ''
    while d != 0:
        s += str(d % 3)
        d //= 3
    return s[::-1]


for N in range(1, 10000):
    R = vtr(N)
    if N % 3 == 0:
        R = '1' + R + '02'
    else:
        R += vtr(N % 3 * 4)
    if int(R, 3) < 199:
        print(N)