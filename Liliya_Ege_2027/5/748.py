l = []
for N in range(1, 10000):
    R = bin(N)[2:]
    # R[:2]
    if '0' in R:
        R = R[::-1].replace('0', R[:2])
        R = int(R, 2)