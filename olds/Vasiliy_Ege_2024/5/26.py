for N in range(1, 10000):
    R = bin(N)[2:]
    if (R.count('1') * 1) % 2 != 0:
        R = R + '11'
    else:
        R = '11' + R
    if int(R, 2) > 102:
        print(N)