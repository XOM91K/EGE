for N in range(2,10000,2):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = '1' + R
        R =R[:-2] + '11'
    else:
        R = '10' + R + '0'
    R = int(R,2)
    if R > 999:
        print(R)