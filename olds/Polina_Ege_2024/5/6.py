for N in range(1000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R = '101' + R[3:] + '0'
    else:
        R = '10' + R[2:] + '11'
    R = int(R, 2)
    if R > 68:
        print(N)