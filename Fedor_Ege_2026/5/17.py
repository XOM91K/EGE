for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = '1' + R[:-2] + '11'
    else:
        R = '10' + R + '0'
    R = int(R,2)
    if R > 999 and N % 2 == 0:
        if R < 1007:
            print(R)