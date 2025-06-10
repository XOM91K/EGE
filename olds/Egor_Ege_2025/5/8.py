for N in range(10, 10 ** 9):
    R = bin(N)[2:]
    if R.count('0') > R.count('1'):
        if '0' in R:
            R = R.replace('0', '1', 1)
    else:
        d = R[::-1].replace('1', '0', 1)[::-1]
    R = int(R, 2)
    R = abs(R - N)
    if R > 1000000:
        print(N, R)
        break