def v5(d):
    s = ''
    while d > 0:
        s = str(d % 5) + s
        d //= 5
    if s == '':
        return '0'
    return s


for N in range(1, 100000):
    R = v5(N)
    if N % 2 == 0:
        R = R + v5(int(R[-1]) * 3)
    else:
        R = R[-1] + R[1:-1] + R[0] + '1'
    R = str(int(R))
    if R.count('0') == 4:
        print(N)
