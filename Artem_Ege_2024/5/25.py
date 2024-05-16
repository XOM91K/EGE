def tr(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
for N in range(1, 10000):
    R = tr(N)
    if N % 2 == 0:
        R = '1' + R + '00'
    else:
        R += tr(R.count('1') * 1 + R.count('2') * 2)
    R = int(R, 3)
    if R > 168:
        print(N)