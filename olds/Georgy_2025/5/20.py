def v3(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    return s[::-1]
for N in range(1, 10000):
    R = v3(N)
    if (R.count("0") + R.count("1") + R.count("2"))%3==0:
        R = "20" + R
    else:
        R = "10" + R
    R = int(R, 3)
    if R < 100:
        print(N)