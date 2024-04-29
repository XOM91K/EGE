for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R += '10'
    else:
        R += '11'
    if R.count('1') % 2 == 0:
        R += R[-1]
    else:
        R += R[-2]
    R = int(R, 2)
    if R > 44:
        print(N)