def ts(n):
    s = ""
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]


for N in range(11, 1000):
    R = ts(N)
    if R.count("2") + R.count("0") > R.count("1"):
        R = "22" + R
    else:
        R = "11" + R
    if int(R, 3) > 100:
        print(int(R, 3))