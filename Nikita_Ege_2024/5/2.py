for N in range(256):
    R = bin(N)[2:]
    R = '0' * (8 - len(R)) + R
    R = R.replace('1', '2')
    R = R.replace('0', '1')
    R = R.replace('2', '0')
    R = int(R, 2)
    if R - N == 111:
        print(N)