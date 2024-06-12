def v5(n):
    ost = ''
    while n > 0:
        ost = ost + str(n % 5)
        n = n // 5
    return ost[::-1]
for N in range(5, 10000):
    R = v5(N)
    if N % 5 == 0:
        R = R + R[-2:]
    else:
        R = R + v5(N % 5 * 7)
    R = int(R, 5)
    if R > 200:
        print(R)
