d = []
for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 4 == 0:
        R += '1111'
    elif R.count('1') % 3 == 0:
        R = '111' + R
    else:
        R += '11'
    R = int(R, 2)
    if R < 450:
        d.append(R)
        print(R)
print(max(d))