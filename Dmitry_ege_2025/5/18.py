#933
mn = 10 ** 10
for N in range(150, 10000):
    R = bin(N)[2:]
    if R[-3:] == '101':
        R = R + '0'
    else:
        R = R + '11'
    R = int(R, 2)
    if R > 405:
        mn = min(mn, R)
print(mn)