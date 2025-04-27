for N in range(1, 10000):
    R = bin(N)[2:]
    if '0' in R:
        R = R[:R.rindex('0')] + R[:2] + R[R.rindex('0') + 1:]
        R = R[::-1]
        R = int(R, 2)
        if R == 123:
            print(N)

# R = '10111011'
# print(R[:R.rindex('0')] + R[:2] + R[R.rindex('0') + 1:])