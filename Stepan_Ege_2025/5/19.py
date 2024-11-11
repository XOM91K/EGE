def v5(d):
    R = ''
    while d > 0:
        R += str(d % 5)
        d //= 5
    return R[::-1]


for N in range(1, 10000):
    R = v5(N)
    if N % 5 == 0:
        R = R + R[-2:]
    else:
        R = R + v5(N % 5 * 7)
    R = int(R, 5)
    if R > 200:
        print(R)