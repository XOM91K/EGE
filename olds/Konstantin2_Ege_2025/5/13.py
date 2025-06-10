def v3(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    return s[::-1]
for N in range(1, 10000):
    R = v3(N)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        R = R + v3(R.count('1') + R.count('2') * 2)
    R = int(R, 3)
    if R % 2 == 0 and R > 220:
        print(R)