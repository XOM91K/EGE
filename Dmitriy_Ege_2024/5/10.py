for N in range(1, 1000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R.replace('0', '11')
    else:
        R = R.replace('1', '10')
    if int(R, 2) <= 161:
        print(int(R, 2))