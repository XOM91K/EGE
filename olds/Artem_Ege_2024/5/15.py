def tr(n):
    s = '0'
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
for N in range(1, 100000):
    R = tr(N)
    R += tr(R.count('2'))
    R += tr(R.count('1'))
    R += tr(R.count('0'))
    R = int(R, 3)
    print(R)
    break
    if R < 1000:
        print(N, R)