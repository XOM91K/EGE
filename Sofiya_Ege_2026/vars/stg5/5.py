d = []
for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R += '0'
        R = '1' + R[2:]
    else:
        R += '1'
        R = '11' + R[2:]
    R = int(R, 2)
    if R < 744:
        d.append(R)
        print(N, R)
print(max(d))