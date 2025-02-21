for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('0') > 0:
        R = R[:R.rindex('0')] + R[:2] + R[R.rindex('0') + 1:]
    R = R[::-1]
    R = int(R, 2)
    if R == 123:
        print(N)
# s = '1010101111'
# s = s[:s.rindex('0')] + s[:2] + s[s.rindex('0') + 1:]
# print(s)
# #s1 = '11011011011111111'
# print(s.index('0'))
# print(s.rindex('0')) #right
# s = 'ПОЛЕ'
# print(s[::-1])