def v3(n):
    s = ''
    while n > 0:
        s += f'{n % 3}'
        n = n // 3
    return s[::-1]
for N in range(1, 10000):
    R = v3(N)
    if N % 3 == 0:
        R += R[-2] + R[-1]
    else:
        R += v3((R.count('1') + R.count('2') * 2) * 2)
    R = int(R, 3)
    if R > 520 and R % 2 != 0:
        print(R)