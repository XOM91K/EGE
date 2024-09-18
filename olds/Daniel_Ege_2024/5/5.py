for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R = '11' + R[2:] + '00'
    else:
        R = '10' + R[2:] + '11'
    if R.count('1') % 2 == 0:
        R = '11' + R[2:] + '00'
    else:
        R = '10' + R[2:] + '11'
    if int(R, 2) < 1500:
        print(int(R, 2))

