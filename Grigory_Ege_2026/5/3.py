d = []
for N in range(1, 1000):
    R = bin(N)[2:]
    if N % 3 == 0:
        #10101100100
        R = R + R[-3:]
    else:
        R = R + bin(N % 3)[2:]
    R = int(R, 2)
    if R < 170:
        d.append(R)
print(max(d))
