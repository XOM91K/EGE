def v3(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    return s[::-1]
for N in range(1, 10000):
    R = v3(N)
    if N % 2 == 0:
        R = '1' + R + '00'
    else:
        R += v3(sum(map(int, R)))
    R = int(R, 3)
    if R > 168:
        print(N)