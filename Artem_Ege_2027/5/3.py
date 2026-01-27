d = []
for N in range(1, 10000):
    R = bin(N)[2:]
    R = R.replace('0', '$')
    R = R.replace('1', '0')
    R = R.replace('$', '1')
    if R.count('1') % 2 == 0:
        R += '0'
    else:
        R += '1'
    R = int(R, 2)
    if R < 170:
        d.append(R)
print(max(d))

# R = 1010100
# R = 1010
# R = 101
# R = '1010111'
# R = R.replace('0', '$')
# R = R.replace('1', '0')
# R = R.replace('$', '1')
# #R = R.replace('0', '1')
# #R = R.replace('1', '0')
# print(R)