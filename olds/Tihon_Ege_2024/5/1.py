for N in range(2, 10000):
    R = bin(N)[2:]
    for i in range(3):
        if R.count('0') == R.count('1'):
            R += R[-1]
        else:
            R += '1' if R.count('0') > R.count('1') else '0'
    R = int(R, 2)
    if N < 70 and R % 4 == 0:
        print(N)

