def v4(d):
    s = ''
    while d > 0:
        s = str(d % 4) + s
        d //= 4
    return s
for N in range(1, 10000):
    R = v4(N)
    if sum(map(int, R)) % 2 == 0:
        R = '13' + R[2:] + '0'
    else:
        R = '2' + R[:-2] + '13'
    R = int(R, 4)
    if R == 167:
        print(N)