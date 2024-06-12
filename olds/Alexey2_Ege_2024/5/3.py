for N in range(0, 256):
    R = bin(N)[2:]
    R = '0' * (8 - len(R)) + R
    R = R.replace('1', '@')
    R = R.replace('0', '1')
    R = R.replace('@', '0')
    if int(R, 2) - N == 111:
        print(N)
