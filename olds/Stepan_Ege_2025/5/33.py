for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 2 != 0:
        R = R.replace('1', '111')
    else:
        R = R.replace('0', '000')
    R = int(R, 2)
    if R > 701 and R < 960:
        print(N, R)