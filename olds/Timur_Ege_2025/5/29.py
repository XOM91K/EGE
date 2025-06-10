for N in range(1,1000):
    R = bin(N)[2:]
    if sum(map(int,str(R))) % 4 == 0:
        R = R + '1111'
    else:
        if sum(map(int, str(R))) % 3 == 0:
            R = '111' + R
        else:
            R = R + '11'
    R = int(R, 2)
    if R < 450 and R > 443:
        print(R)