for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') > R.count('0'):
        R = '1' + R + '00'
    else:
        R = R + '11'
        R = int(R, 8)
        if R >= 420:
            print(N)