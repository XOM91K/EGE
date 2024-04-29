def tr(d):
    s = ''
    while d != 0:
        s += str(d % 3)
        d //= 3
    s = s[::-1]
    return s
for N in range(1, 10000):
    R = tr(N)
    if N % 3 != 0:
        R += tr(N % 3 * 5)
    if int(R, 3) > 146:
        print(N)