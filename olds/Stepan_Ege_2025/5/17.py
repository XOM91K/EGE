def v3(N):
    s = ''
    while N > 0:
        s += str(N % 3)
        N //= 3
    return s[::-1]
for N in range(1, 10000):
    R = v3(N) #220
    if (R.count('1') + R.count('2') * 2) % 3 == 0:
        R = '20' + R
    else:
        R = '10' + R
    R = int(R, 3)
    if R < 100:
        print(N)