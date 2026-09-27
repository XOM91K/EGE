for N in range(1, 10000):
    R = bin(N)[2:]
    if '0' in R:
        ind = R.rindex('0')
        lt = R[:ind]
        rt = R[ind + 1:]
        R = lt + R[:2] + rt
        R = R[::-1]
        R = int(R, 2)
        if R == 123:
            print(N)

