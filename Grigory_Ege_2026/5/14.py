for N in range(1, 10000):
    R = bin(N)[2:]
    R = R.replace('0', 'x')
    R = R.replace('1', '0')
    R = R.replace('x', '1')
    R = int(R, 2)
    R = N - R
    if R == 1005:
        print(N)