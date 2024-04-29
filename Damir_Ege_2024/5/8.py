for N in range(1, 1000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R = '10' + R[2:] + '0'
    else:
