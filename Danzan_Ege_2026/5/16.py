def v4(d):
    s = ''
    while d > 0:
        s += str(d%4)
        d //= 4
    if s == '':
        return '0'
    return s[::-1]
for N in range(0, 10000):
    R = v4(N)
    if N % 2 == 0:
        R = '12' + R + v4(3*int(R[-1]))
    else:
        R = '13' + R + '21'
    R = int(R, 4)
    if int(R) > 50:
        print(R)