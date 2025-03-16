for N in range(1, 10000):
    R = bin(N)[2:]
    R = R.replace('0', '#')
    R = R.replace('1', '0')
    R = R.replace('#', '1')
    R = int(R, 2)
    R = abs(R - N)
    if R == 1005:
        print(N)