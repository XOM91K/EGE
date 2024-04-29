for N in range(1, 10000):
    s = ''
    d = N
    while d != 0:
        s += str(d % 3)
        d //= 3
    R = s[::-1]
    if N % 3 == 0:
        R = '1' + R + '02'
    else:
        d1 = N % 3 * 4
        s = ''
        while d1 != 0:
            s += str(d1 % 3)
            d1 //= 3
        R += s[::-1] #21012012010
    if int(R, 3) < 199:
        print(N)