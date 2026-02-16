for N in range(1, 10000):
    R = bin(N)[2:]
    R = R.replace('1', '#')
    R = R.replace('0', '1')
    R = R.replace('#', '0')
    # R = str(int(R))
    R = int(R, 2)
    if N - R == 1005:
        print(N)
        break