def tr(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    return s[::-1]
for N in range(1, 1000):
    R = tr(N)
    if N % 4 == 0:
        R = R + R[-3:]
    else:
        R = R + tr((N % 4) * 4)
    R = int(R, 3)
    if R < 127:
        print(R)