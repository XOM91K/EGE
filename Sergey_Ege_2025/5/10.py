for d in range(1, 10000):
    R = [bin(int(x))[2:].zfill(4) for x in str(d)]
    R = [x + '1' if x.count('1') % 2 != 0 else x + '0' for x in R]
    R = ''.join(R)
    R = '1' + R[2:] + '0'
    if int(R, 2) == 674890:
        print(d)