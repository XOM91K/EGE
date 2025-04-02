def v3(d):
    s = ''
    while d > 0:
        s = str(d % 3) + s
        d //= 3
    return s

for N in range(1, 10000):
    R = v3(N)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += v3(sum(map(int, R)))
    R = int(R, 3)
    if R > 220:
        print(R)