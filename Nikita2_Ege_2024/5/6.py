def pac(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    return s[::-1]

for N in range(1, 10000):
    R = pac(N) # 2101
    if (R.count('2') * 2 + R.count('1')) % 3 == 0:
        R = '20' + R
    else:
        R = '10' + R
    if int(R, 3) < 100:
        print(N)