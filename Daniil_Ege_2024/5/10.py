def tr(N):
    s = ''
    while N > 0:
        s += str(N % 3)
        N //= 3
    return s[::-1]
for N in range(1, 1000):
    R = tr(N)
    if (R.count('1') + R.count('2') * 2) % 4 == 0:
        R = '1' + R[:-2]
    else:
        R = R + tr((R.count('1') + R.count('2') * 2) % 4 * 3)
    if int(R, 3) > 353:
        print(int(R, 3))