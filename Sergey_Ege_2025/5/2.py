l = []
for N in range(1, 1000):
    R = bin(N)[2:]
    if R.count('1') % 2 != 0:
        R += '11'
    else:
        R += '00'
    R = int(R, 2)
    if R > 114:
        l.append(R)
print(min(l))