ct = 0
for N in range(11, 10000):
    R = bin(N)[2:]
    if N % 10 == 0:
        R += R[-4:]
    else:
        R += bin(((int(str(N)[-1]) ** 2) // 2))[2:]
    R = int(R, 2)
    if R < 680:
        print(N)
        ct += 1
print(ct)