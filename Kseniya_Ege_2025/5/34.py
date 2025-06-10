for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = '101' + R[3:]
    else:
        R = R[:-3] + '111'
    R = int(R, 2)
    if R > 30 and N <= 34:
        print(R)