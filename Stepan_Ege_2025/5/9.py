for N in range(1, 10000):
    R = ''
    d = N
    while d > 0:
        R += str(d % 3)
        d //= 3
    R = R[::-1]
    # R = '120100'
    if (R.count('1') + R.count('2') * 2) % 3 == 0:
        R = '20' + R
    else:
        R = '10' + R
    R = int(R, 3)
    if R < 100:
        print(N)