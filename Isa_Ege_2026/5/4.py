l = []
for N in range(1, 10000):
    R = bin(N)[2:]
    R = R.replace('1', '#')
    R = R.replace('0', '1')
    R = R.replace('#', '0')
    # R += '0' if R.count('1') % 2 == 0 else '1'
    if R.count('1') % 2 == 0:
        R += '0'
    else:
        R += '1'
    R = int(R, 2)
    if R < 170:
        l.append(R)
print(max(l))