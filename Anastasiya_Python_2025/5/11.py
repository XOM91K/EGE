d = []
for N in range(1, 100000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R += '1'
    else:
        R = '1' + R + '0'
    R = int(R, 2)
    if R > 666:
        d.append(R)
print(min(d))