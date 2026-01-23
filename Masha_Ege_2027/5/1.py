for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R += '0'
    else:
        R += '1'
    if R.count('1') % 2 == 0:
        R += '0'
    else:
        R += '1'
    R = int(R, 2)
    print(R)
# s = 'abracadabra'
# print(s[::-1])
# print(s[2:])
# print(s[-3:])
# print(s[0] + s[1] + s[2] + s[3])
# print(s[0:4])