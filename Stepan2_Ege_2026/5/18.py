for N in range(1,10000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        R = '1' + R + '1'
    R = int(R, 2)
    if R > 700 and R < 769:
        print(R)