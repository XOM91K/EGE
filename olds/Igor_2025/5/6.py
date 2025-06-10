def v3(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    return s[::-1]
for N in range(1, 100_000_000):
    R = v3(N)
    R = R.replace('0', '#')
    R = R.replace('2', '0')
    R = R.replace('#', '2')
    R = int(R, 3)
    R = abs(N - R)
    if R == 1_864_246:
        print(N)
