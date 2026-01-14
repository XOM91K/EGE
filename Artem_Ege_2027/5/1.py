for N in range(1, 10000):
    R = bin(N)[2:] # 11010  10010
    if R.count('1') % 2 == 0:
        R = R + '0'
        R = '10' + R[2:]
    else:
        R = R + '1'
        R = '11' + R[2:]
    R = int(R, 2)
    if N > 27:
        print(R)