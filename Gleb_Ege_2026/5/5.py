for N in range(1, 1000):
    R = bin(N)[3:]
    if R.count('1') % 2 == 0:
        R = '10' + R
    else:
        R = '1' + R + '0'
    R = int(R, 2)
    if R < 450:
        print(R)