for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R = '101' + R[3:] + '01'
    else:
        R = '111' + R[3:] + '10'
    R = int(R, 2)
    if R < 385:
        print(N)