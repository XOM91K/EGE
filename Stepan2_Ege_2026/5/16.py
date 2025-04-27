for N in range(2, 10000):
    R = bin(N)[2:]
    if R.count('0') == R.count('1'):
        R += R[-1]
    else:
        if R.count('0') < R.count('1'):
            R += '0'
        else:
            R += '1'
    if R.count('0') == R.count('1'):
        R += R[-1]
    else:
        if R.count('0') < R.count('1'):
            R += '0'
        else:
            R += '1'
    if R.count('0') == R.count('1'):
        R += R[-1]
    else:
        if R.count('0') < R.count('1'):
            R += '0'
        else:
            R += '1'
    R = int(R, 2)
    if N > 154 and R % 7 == 0:
        print(N)