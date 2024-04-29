for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R += '00'
        R = '11'+ R[2:]
    else:
        R += '11'
        R = '10' + R[2:]
    if R.count('1') % 2 == 0:
        R += '00'
        R = '11' + R[2:]
    else:
        R += '11'
        R = '10' + R[2:]
    if int(R, 2) > 1500:
        print(int(R, 2))