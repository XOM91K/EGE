def v2(d):
    s = bin(d)[2:]
    return s
a = []
for N in range(1,10000):
    R = v2(N)
    if N%2 == 0:
        R = R + '0'
    else:
        R = R + '1'
    if R.count('1') % 2 == 0:
        R = R + '0'
    else:
        R = R + '1'
    R = int(R, 2)
    if R > 2023:
        a.append(R)
print(min(a))