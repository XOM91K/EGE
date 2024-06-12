for N in range(2, 10000):
    R = bin(N)[2:]
    R = R[1:]
    R = R.replace('0', '$')
    R = R.replace('1', '0')
    R = R.replace('$', '1')
    R = '1' + R
    R = int(R, 2)
    R += N
    if N % 2 != 0 and R > 99:
        print(N)