def v5(d):
    s = ''
    if d == 0:
        return '0'
    while d > 0:
        s += str(d % 5)
        d //= 5
    return s[::-1]
for N in range(0, 10000):
    R = v5(N)
    if N % 2 == 0:
        R += v5(int(R[-1]) * 3)
    else:
        R = R[-1] + R[1:-1] + R[0] + '1'
    R = str(int(R))
    if R.count('0') == 4:
        print(N)

