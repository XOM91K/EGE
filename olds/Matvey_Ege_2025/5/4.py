def v5(N):
    s = ''
    while N > 0:
        s += str(N % 5)
        N //= 5
    return s[::-1]
for N in range(5, 10000):
    R = v5(N)
    if N % 5 == 0:
        R += R[-2:]
    else:
        R += v5(N % 5 * 7)
    R = int(R, 5)
    if R > 200:
        print(R)