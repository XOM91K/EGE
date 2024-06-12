def v6(d):
    R = ''
    while d > 0:
        R += str(d % 6)
        d //= 6
    return R[::-1]
for N in range(1, 10000):
    R = v6(N)
    if N % 3 == 0:
        R += R[:2]
    else:
        R += v6(N % 3 * 10)
    if int(R, 6) > 680:
        print(int(R, 6))