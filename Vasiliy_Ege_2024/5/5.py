for N in range(128, 256):
    R = bin(N)[2:]
    R = R.replace('1', '~')
    R = R.replace('0', '1')
    R = R.replace('~', '0')
    if (N - int(R, 2)) == 105:
        print(N)