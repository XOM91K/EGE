mx = 0
for n in range(1,1000):
    R = bin(n)[2:]
    R = R.replace('1', '@')
    R = R.replace('0', '1')
    R = R.replace('@', '0')
    if R.count('1') % 2 == 0:
        R += '0'
    else:
        R += '1'
    R = int(R, 2)
    if R < 170:
        print(R)
        mx = max(R, mx)
print(mx)