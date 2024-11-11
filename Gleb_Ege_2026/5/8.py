for N in range(1, 10000):
    R = bin(N)[2:]
    if '0' in R:
        ind = R.rindex('0')
        R = R[:ind] + R[:2] + R[ind + 1:]
        R = R[::-1]
        R = int(R, 2)
        if R == 123:
            print(N)

# d = '99836120831111111111111'
# ind = d.rindex('0')
# d = d[:ind] + d[:2] + d[ind + 1:]
# print(d, ind)