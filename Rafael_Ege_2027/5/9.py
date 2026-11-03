for N in range(1,10000):
    R = bin(N)[2:]
    R = R.replace('0','2')
    R = R.replace('1','0')
    R = R.replace('2','1')
    R = int(R, 2)
    if N - R == 1005:
        print(N)