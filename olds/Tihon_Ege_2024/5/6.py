for N in range(2, 10000):
    R = bin(N)[2:]
    for x in range(3):
        if R.count('0') == R.count('1'):
            R += R[-1]
        else:
            if R.count('0') > R.count('1'):
                R += '1'
            else:
                R += '0'
    R = int(R, 2)
    if N < 100 and R % 2 == 0 and R % 4 != 0:
        print(N)
