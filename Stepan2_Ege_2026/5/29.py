def v7(d):
    s = ''
    while d > 0:
        s = str(d % 7) + s
        d //= 7
    return s
for N in range(0, 1001):
    R = v7(N)
    if N % 2 == 0:
        R = '52' + R + '1'
    else: # 34502   2     3
        R = R[-1] + R[1:-1] + R[0] + '15'
    R = int(R)
    if len(str(R)) == 4:
        print(N, R)