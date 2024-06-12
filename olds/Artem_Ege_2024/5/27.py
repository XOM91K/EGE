def tr(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
for N in range(1, 10000):
    R = tr(N)
    if (R.count('1') + R.count('2') * 2) % 2 == 0:
        R = '2' + R[2:] + '0'
    else:
        R = '20' + R[2:] + '1'
    R = int(R, 3)
    if R > 75:
        print(N, R)