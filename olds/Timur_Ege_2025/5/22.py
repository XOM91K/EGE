def v4(d):
    s = ''
    while d > 0:
        s += str(d % 4)
        d //= 4
    return s[::-1]
for N in range(1, 10000):
    R = v4(N)
    if len(R) % 2 == 0:
        R = R[:len(R) // 2] + '0' + R[len(R) // 2:]
    if int(R) <= 180:
        print(N)