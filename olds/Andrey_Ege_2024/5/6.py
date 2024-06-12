for N in range(2, 1000):
    R = bin(N)[2:]
    if '0' in R:
        R = R[:R.rfind('0')] + R[:2] + R[R.rfind('0') + 1:]
    else:
        continue
    R = R[::-1]
    R = int(R, 2)
    if R == 127:
        print(N)