for N in range(2, 1000):
    R = bin(N)[2:]
    if R.count('0') == R.count('1'):
        R = R + R[-1]
    else:
        if R.count('0') < R.count('1'):
            R = R + '0'
        else:
            R = R + '1'
    if R.count('0') == R.count('1'):
        R = R + R[-1]
    else:
        if R.count('0') < R.count('1'):
            R = R + '0'
        else:
            R = R + '1'
    if R.count('0') == R.count('1'):
        R = R + R[-1]
    else:
        if R.count('0') < R.count('1'):
            R = R + '0'
        else:
            R = R + '1'
    R = int(R, 2)
    if N < 70 and R % 4 == 0:
        print(N)
