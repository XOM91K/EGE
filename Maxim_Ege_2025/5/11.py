for N in range(1, 10000):
    d = N
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    R = s[::-1]
    if N % 2 == 0:
        R = '1' + R + '00'
    else:
        s1 = ''
        g = sum(map(int, R))
        while g > 0:
            s1 += str(g % 3)
            g //= 3
        R += s1[::-1]
    R = int(R, 3)
    if R > 168:
        print(N)