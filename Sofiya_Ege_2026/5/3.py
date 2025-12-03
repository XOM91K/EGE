def v4(N):
    s = ''
    while N > 0:
        s += str(N % 4)
        N //= 4
    return s[::-1]
for N in range(1, 100000):
    R = v4(N)
    if N % 4 == 0:
        R = R[:-1] + '13'
    else:
        R = '2' + R + str(N % 4)
    R = int(R, 4)
    if R >= 196:
        print(N)