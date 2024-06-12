for N in range(1, 10000):
    R = bin(N)[2:]
    R = R.replace('0', '#')
    R = R.replace('1', '0')
    R = R.replace('#', '1')
    R = N - int(R, 2)
    if R == 979:
        print(N)

