T = []
for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R += '11'
    else:
        R += '01'
    R = int(R, 2)
    if R > 61:
        T.append(R)
print(min(T))
