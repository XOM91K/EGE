def v6(d):
    s = ''
    while d > 0:
        s += str(d % 6)
        d //= 6
    return s[::-1]
for N in range(1, 10000):
    R = v6(N)
    if N % 3 == 0:
        R += R[::-1]
    else:
        R += v6(sum(map(int, R)))
    R = int(R, 6)
    if N > 25 and R % 2 == 0 and R < 225:
        print(R)