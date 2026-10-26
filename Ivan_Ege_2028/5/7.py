for N in range(1,100000):
    R = bin(N)[2:]
    if R.count("1") % 2 ==0:
        R = R + R[-2:]
    else:
        rz = R[-2:]
        rz = rz.replace('0', '#')
        rz = rz.replace('1', '0')
        rz = rz.replace('#', '1')
        R = R + rz
    R = int(R, 2)
    if R > 154:
        print(N)