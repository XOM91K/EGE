for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R += R[-2:]
    else:
        RR = R[-2:]
        RR = RR.replace('0', '#')
        RR = RR.replace('1', '0')
        RR = RR.replace('#', '1')
        R += RR
    R = int(R, 2)
    if R > 154:
        print(N)