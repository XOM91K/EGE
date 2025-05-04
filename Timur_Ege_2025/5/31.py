def v4(d):
    s = ''
    if d == 0:
        return '0'
    while d > 0:
        s += str(d % 4)
        d //= 4
    return s[::-1]
for N in range(96, 100000):
    R = v4(N)
    if N % 2 == 0:
        R = '12' + R + v4(int(R[-1]) * 3)
    else:
        R = '13' + R + '21'
    R = int(R, 4)
    if R > 50 and R < 500:
        print(R)
import math
print(math.log2(10))