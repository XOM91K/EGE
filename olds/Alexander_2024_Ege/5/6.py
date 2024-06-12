for N in range(1, 1000000):
    R = bin(N)[2:]
    d = N
    if d % 3 == 0:
        R += '11'
    else:
        R += '1'
    d = int(R, 2)
    if d % 5 == 0:
        R += '101'
    else:
        R += '1'
    R = int(R, 2)
    if R < 10 ** 6:
        print(N)