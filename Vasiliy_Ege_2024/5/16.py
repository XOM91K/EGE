def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n = n // 3
    return s[::-1]
for N in range(1, 10000):
    R = v3(N)
    if N % 4 == 0:
        R += R[-3:]
    else:
        R += v3(N % 4 * 4)
    R = int(R, 3)
    if R < 127:
        print(R)