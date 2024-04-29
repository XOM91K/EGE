def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
mn = 10 ** 10
for N in range(1, 10000):
    R = v3(N)
    if (R.count('1') + R.count('2') * 2) % 4 == 0:
        R = '1' + R[:-2]
    else:
        R += v3((R.count('1') + R.count('2') * 2) % 4 * 3)
    R = int(R, 3)
    if R > 353:
        print(R)