def v7(d):
    s = ''
    while d > 0:
        s += str(d % 7)
        d //= 7
    return s[::-1]
for N in range(1, 10000):
    R = v7(N)
    if R.count('2') % 2 == 0:
        R += '555'
    else:
        R = '1' + R
    R = int(R, 7)
    if R < 3799:
        print(N)