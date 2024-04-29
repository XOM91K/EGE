for N in range(11, 10000):
    d = N
    R = ''
    while d > 0:
        R += str(d % 3)
        d //= 3
    R = R[::-1]
    if (R.count('0') + R.count('2')) > R.count('1'):
        R = '22' + R
    else:
        R = '11' + R
    if int(R, 3) > 100:
        print(int(R, 3))