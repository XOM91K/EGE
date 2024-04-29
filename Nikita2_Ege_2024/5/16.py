for N in range(10, 10000):
    R = oct(N)[2:]
    if (R.count('1') * 1 + R.count('2') * 2 + R.count('3') * 3 + R.count('4') * 4 + R.count('5') * 5 + R.count('6') * 6 + R.count('7') * 7) % 2 == 0:
        R = R + str(N % 3)
    else:
        R = str(max(map(int, R))) + R
    if int(R, 8) >= 127:
        print(N)