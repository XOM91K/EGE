for N in range(0, 1000):
    R= bin(N)[2:]
    if sum(map(int, R)) % 4 == 0:
        R = R + '1111'
    elif sum(map(int, R)) % 3 == 0:
        R = '111' + R
    else:
        R = R + '11'
    R = int(R, 2)
    if R < 450:
        print(R)