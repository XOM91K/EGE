def tr(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
for N in range(1, 10000):
    R = tr(N) #211
    if (R.count('1') + R.count('2') * 2) % 3 == 0:
        R = '20' + R
    else:
        R = '10' + R
    if int(R, 3) < 100:
        print(N)