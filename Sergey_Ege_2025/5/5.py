mx = 0
for N in range(1, 1000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R = '11' + R[2:] + '00'
    else:
        R = '10' + R[2:] + '11'
    if R.count('1') % 2 == 0:
        R = '11' + R[2:] + '00'
    else:
        R = '10' + R[2:] + '11'
    if int(R, 2) < 1500:
        mx = max(mx, int(R, 2))
print(mx)