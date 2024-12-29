for N in range(1, 10000):
    R = bin(N)[2:]
    if '0' in R: # right
        ind = R.rindex('0')
        R = R[:ind] + R[:2] + R[ind + 1:]
        R = R[::-1]
        R = int(R, 2)
        if R == 123:
            print(N)
