d = []
for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = '1' + R + '0'
    else:
        R = '11' + R + '11' # 63
    R = int(R, 2)
    if R > 48:
        d.append(R)
print(min(d))