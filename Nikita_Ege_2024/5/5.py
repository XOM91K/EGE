ct = 0
for N in range(100, 201):
    R = bin(N)[2:]
    if len(R) % 2 == 0:
        R += '10'
    else:
        R = '11' + R
    if int(R, 2) % 2 == 0:
        ct += 1
print(ct)