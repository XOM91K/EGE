ct = 0
for N in range(11, 10000):#248
    R = bin(N)[2:]
    if N % 10 == 0:
        R = R + R[-4:]
    else:
        R = R + bin((int(str(N)[-1]) ** 2) // 2)[2:]
    R = int(R, 2)
    if R < 680:
        ct += 1
print(ct)