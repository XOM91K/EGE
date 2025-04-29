def v5(a):
    s = ''
    if a == 0:
        return '0'
    while a > 0:
        s += str(a % 5)
        a //= 5
    return s[::-1]
for N in range(1,100000):
    R = v5(N)
    if N % 2 == 0:
        R = R + v5(int(R[-1]) * 3)
    else:
        R = R[-1] + R[1:-1] + R[0] + '1'
    R = str(int(R))
    if R.count('0') == 4:
        print(N, R)
# R = '0000000101010101010101111110101'
# R = str(int(R))
# print(R)