for N in range(1, 10000):
    R = bin(N)[2:] # 57 R = 1101010
    if (R.count('0') + R.count('1')) % 2 == 0:
        R = R + '1'
    else:
        R = "1" + R
        R = R + '0'
    R = int(R, 2)
    if R > 666 and R < 1030:
        print(R)
